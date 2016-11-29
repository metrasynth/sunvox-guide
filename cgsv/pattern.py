from collections import defaultdict

from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import unchanged_required
from rv.api import Note, NOTECMD, Pattern


def project_patterns_map():
    return defaultdict(dict)


class PatternDirective(Directive):

    has_content = True
    option_spec = dict(
        pos=unchanged_required,
        map=unchanged_required,
    )
    required_arguments = 1

    def run(self):
        env = self.state.document.settings.env
        if not hasattr(env, 'file_projects_patterns'):
            env.file_projects_patterns = defaultdict(project_patterns_map)
        src_path = self.state.document['source']
        varname, = self.arguments
        projname, patname = varname.split('.')
        p = env.file_projects[src_path]
        project = p[projname]
        pm = env.file_projects_modules[src_path]
        mods = pm[projname]
        pat = Pattern()
        pat.x, pat.y = self.pattern_pos(self.options['pos'])
        modmap = dict(self.module_map(self.options['map'], mods))
        self.write_pattern(pat, self.content, modmap)
        project += pat
        pp = env.file_projects_patterns[src_path]
        pp[patname] = pat
        return []

    def pattern_pos(self, src):
        coords = src.replace(' ', '').split(',')
        x, y = coords
        return int(x), int(y)

    def module_map(self, src, mods):
        members = src.replace(' ', '').split(',')
        for member in members:
            alias, modname = member.split('=')
            alias = int(alias, 16)
            mod = mods[modname]
            yield alias, mod

    def write_pattern(self, pattern, src_lines, modmap):
        tracks = [
            # {
            #     'NN': 16,
            #     'VV': 18,
            #     'MM': 20,
            #     ...,
            # },
        ]
        # Extract note sections from header.
        header, body = src_lines[0], src_lines[1:]
        cur_track = None
        for col in range(len(header)):
            colname = header[col:col + 2]
            if colname == 'NN':
                new_track = {'NN': col}
                tracks.append(new_track)
                cur_track = new_track
            elif colname in ['VV', 'MM', 'CC', 'EE', 'XX', 'YY']:
                cur_track[colname] = col
        # Set the shape of the pattern.
        pattern.tracks = len(tracks)
        pattern.lines = len(body)
        pattern.clear()
        # Extract notes.
        for line_no, line_src in enumerate(body):
            for track_no, track in enumerate(tracks):
                note = pattern.data[line_no][track_no]
                assert isinstance(note, Note)
                for colname, offset in track.items():
                    src = line_src[offset:offset+2]
                    if colname == 'NN':
                        if src == 'SP':
                            note.note = NOTECMD.SET_PITCH
                        elif src == '<<':
                            note.note = NOTECMD.PREV_TRACK
                        elif src == '==':
                            note.note = NOTECMD.NOTE_OFF
                        elif (
                            src[0].lower() in 'abcdefg'
                            and src[1] in '0123456789'
                        ):
                            note.note = getattr(NOTECMD, src)
                    else:
                        try:
                            value = int(src, 16)
                        except ValueError:
                            value = None
                        else:
                            if colname == 'VV':
                                note.vel = value + 1
                            elif colname == 'MM':
                                if value in modmap:
                                    value = modmap[value].index
                                note.module = value + 1
                            elif colname == 'CC':
                                note.controller = value
                            elif colname == 'EE':
                                note.effect = value
                            elif colname == 'XX':
                                note.val_xx = value
                            elif colname == 'YY':
                                note.val_yy = value

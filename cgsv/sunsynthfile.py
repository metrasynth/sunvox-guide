import os
from textwrap import dedent

from docutils.parsers.rst.directives import unchanged_required

from rv.api import Synth

from .directive import Directive


class SunsynthFileDirective(Directive):

    has_content = True
    option_spec = dict(
        filename=unchanged_required,
    )
    required_arguments = 1

    def run(self):
        env = self.state.document.settings.env
        builder = env.app.builder

        layout = self.options.get('layout')
        filename = self.options['filename']

        src_path = self.state.document['source']
        varname, = self.arguments
        projname, modname = varname.split('.')

        p = env.file_projects[src_path]
        project = p[projname]
        pm = env.file_projects_modules[src_path]
        mod = pm[projname][modname]

        synth = Synth(mod)

        if not filename.endswith('.sunsynth'):
            filename += '.sunsynth'
        filename = env.docname.replace('/', '-') + '-' + filename
        basedir = os.path.join(builder.srcdir, '_sunvox_files')
        os.makedirs(basedir, exist_ok=True)
        filepath = os.path.join(basedir, filename)

        with open(filepath, 'wb+') as f:
            synth.write_to(f)
            filesize = f.tell()

        download_link = dedent("""
        :download:`Download {} </_sunvox_files/{}>`
        """).format(synth.module.name or synth.module.mtype, filename)

        return self._parse(download_link, '<sunsynthfile>')

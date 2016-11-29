import os
from textwrap import dedent

from docutils.parsers.rst.directives import unchanged_required

from .directive import Directive

try:
    import numpy as np
    from scipy.io import wavfile
    from sunvox.api import Slot
    from sunvox.buffered import BufferedProcess
except (ImportError, OSError):
    np = None


class ProjectAudioDirective(Directive):

    has_content = True
    option_spec = dict(
        filename=unchanged_required,
        start=float,
        duration=float,
        fadeout=float,
    )
    required_arguments = 1

    def run(self):
        env = self.state.document.settings.env
        builder = env.app.builder

        layout = self.options.get('layout')
        filename = self.options['filename']

        src_path = self.state.document['source']
        projname, = self.arguments
        p = env.file_projects[src_path]
        project = p[projname]

        if not filename.endswith('.wav'):
            filename += '.wav'
        filename = env.docname.replace('/', '-') + '-' + filename
        basedir = os.path.join(builder.srcdir, '_sunvox_files')
        os.makedirs(basedir, exist_ok=True)
        filepath = os.path.join(basedir, filename)

        if np is not None:
            freq = BufferedProcess.freq
            start = int(self.options['start'] * freq)
            duration = int(self.options['duration'] * freq)
            fadeout = int(self.options['fadeout'] * freq)
            length = start + duration
            output = np.zeros((length, 2), BufferedProcess.data_type)
            process = BufferedProcess()
            slot = Slot(project, process=process)
            position = 0
            slot.play_from_beginning()
            while position < length:
                buffer = process.fill_buffer()
                end_pos = min(position + BufferedProcess.size, length)
                copy_size = end_pos - position
                output[position:end_pos] = buffer[:copy_size]
                position = end_pos
            process.kill()

            # Clip start
            output = output[start:length]

            # Fade out
            fader = np.linspace(
                1.0, 0.0, fadeout, dtype=BufferedProcess.data_type)
            fader = np.repeat(fader, 2).reshape((fadeout, 2))
            output[-fadeout:] *= fader

            wavfile.write(filepath, freq, output)

        download_link = dedent("""
        :download:`Download Audio for {} </_sunvox_files/{}>`
        """).format(project.name or 'Project', filename)

        return self._parse(download_link, '<svprojectaudio>')

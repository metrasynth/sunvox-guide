import os
from textwrap import dedent

from docutils.parsers.rst.directives import unchanged, unchanged_required

from .directive import Directive


class SunvoxFileDirective(Directive):

    has_content = True
    option_spec = dict(
        layout=unchanged,
        filename=unchanged_required,
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

        if layout == 'auto':
            project.layout()

        if not filename.endswith('.sunvox'):
            filename += '.sunvox'
        filename = env.docname.replace('/', '-') + '-' + filename
        basedir = os.path.join(builder.srcdir, '_sunvox_files')
        os.makedirs(basedir, exist_ok=True)
        filepath = os.path.join(basedir, filename)

        with open(filepath, 'wb+') as f:
            project.write_to(f)
            filesize = f.tell()

        download_link = dedent("""
        :download:`Download {} </_sunvox_files/{}>`
        """).format(project.name or 'Project', filename)

        print(self)
        print(self.state.document['source'])
        print(self.arguments)
        print(self.options)
        print(self.content)
        print('filesize', filesize, 'at', filepath)
        print()

        return self._parse(download_link, '<sunvoxfile>')

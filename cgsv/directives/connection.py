from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import unchanged_required


class ConnectionDirective(Directive):

    has_content = True
    option_spec = dict(
        source=unchanged_required,
        dest=unchanged_required,
    )
    required_arguments = 1

    def run(self):
        env = self.state.document.settings.env
        src_path = self.state.document['source']
        varname, = self.arguments
        pm = env.file_projects_modules[src_path]
        mods = pm[varname]
        source = mods[self.options['source']]
        if self.options['dest'] == 'output':
            p = env.file_projects[src_path]
            project = p[varname]
            dest = project.output
        else:
            dest = mods[self.options['dest']]
        source >> dest
        return []

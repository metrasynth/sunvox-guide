from collections import defaultdict

from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import unchanged
from rv.api import Project


def project_map():
    return defaultdict(Project)


class ProjectDirective(Directive):

    has_content = True
    option_spec = dict(
        name=unchanged,
    )
    required_arguments = 1

    def run(self):
        env = self.state.document.settings.env
        if not hasattr(env, 'file_projects'):
            env.file_projects = defaultdict(project_map)
        src_path = self.state.document['source']
        p = env.file_projects[src_path]
        varname, = self.arguments
        project = p[varname]
        if 'name' in self.options:
            project.name = self.options['name']
        print(self)
        print(self.state.document['source'])
        print(self.arguments)
        print(self.options)
        print(self.content)
        print(project)
        print()
        return []

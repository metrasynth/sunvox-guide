import os
from collections import defaultdict

from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import unchanged
from rv.api import Project, read_sunvox_file


def project_map():
    return defaultdict(Project)


class ProjectDirective(Directive):

    has_content = True
    option_spec = dict(
        name=unchanged,
        filename=unchanged,
    )
    required_arguments = 1

    def run(self):
        env = self.state.document.settings.env
        if not hasattr(env, 'file_projects'):
            env.file_projects = defaultdict(project_map)
        src_path = self.state.document['source']
        p = env.file_projects[src_path]
        varname, = self.arguments
        filename = self.options.get('filename')
        if not filename:
            project = p[varname]
        else:
            if not filename.endswith('.sunvox'):
                filename += '.sunvox'
            _, filepath = env.relfn2path(filename)
            project = read_sunvox_file(filepath)
            p[varname] = project
        if 'name' in self.options:
            project.name = self.options['name']
        return []

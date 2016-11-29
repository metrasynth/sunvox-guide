from collections import defaultdict
from textwrap import indent

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import unchanged
from docutils.statemachine import StringList


UML_FORMATTING = """
!define Synth(name,mtype,desc) class name as "desc" << (S,#FFAAAA) "mtype" >>
!define Effect(name,mtype,desc) class name as "desc" << (E,#FFAAAA) "mtype" >>
!define Misc(name,mtype,desc) class name as "desc" << (M,#FFAAAA) "mtype" >>
!define Output(name,mtype,desc) class name as "desc" << (O,#FFAAAA) "mtype" >>
hide methods
"""


def cval(value):
    if hasattr(value, 'name'):
        return value.name
    else:
        return value


class ModuleGraphDirective(Directive):

    has_content = True
    option_spec = dict(
        style=unchanged,
        depth=unchanged,
    )
    required_arguments = 1

    def run(self):
        env = self.state.document.settings.env
        style = self.options.get('style', 'detailed')
        depth = self.options.get('depth')
        src_path = self.state.document['source']
        varname, = self.arguments
        if '.' in varname:
            projname, modname = varname.split('.')
        else:
            projname, modname = varname, None
        p = env.file_projects[src_path]
        project = p[projname]
        pm = env.file_projects_modules[src_path]
        mod = pm[projname][modname] if modname else None
        if depth is None:
            modules = project.modules
            connections = project.module_connections
        elif int(depth) == 0:
            modules = [mod]
            connections = defaultdict(list)
        else:
            modules = []
            connections = []
        uml_src = [UML_FORMATTING]
        if style == 'basic':
            uml_src += ['hide attributes']
        for module in modules:
            modname = 'mod{:02X}'.format(module.index)
            modtitle = '[{:02X}] {}'.format(module.index, module.name)
            modtype = module.mtype
            modgroup = module.mgroup
            uml_src += [
                '{}({}, "{}", "{}") {{'.format(modgroup, modname,
                                               modtype, modtitle),
                '\n'.join('{} : {}'.format(cname, cval(getattr(module, cname)))
                          for cname in module.controllers),
                '}',
            ]
        for dest, sources in connections.items():
            for src in sources:
                uml_src.append('mod{:02X} --> mod{:02X}'.format(src, dest))
        uml_src = '\n'.join(uml_src)
        uml_src = '..  uml::\n\n' + indent(uml_src, '    ')
        uml = StringList(
            initlist=uml_src.split('\n'),
            parent=self,
            parent_offset=self.content_offset,
        )
        node = nodes.Element()
        node.document = self.state.document
        self.state.nested_parse(uml, 0, node)
        print(self)
        print(self.state.document['source'])
        print(self.arguments)
        print(self.options)
        print(self.content)
        print(uml_src)
        print()
        return list(node)

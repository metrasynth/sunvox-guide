from docutils.nodes import literal_block
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import unchanged


class PatternTableDirective(Directive):

    has_content = True
    option_spec = dict(
        style=unchanged,
    )
    required_arguments = 1

    def run(self):
        env = self.state.document.settings.env
        style = self.options.get('style', 'full')
        if style == 'full':
            style = 'NN VV MM CC EE XXYY'
        src_path = self.state.document['source']
        varname, = self.arguments
        projname, patname = varname.split('.')
        pp = env.file_projects_patterns[src_path]
        pat = pp[patname]
        return [literal_block('', pat.tabular_repr(style))]

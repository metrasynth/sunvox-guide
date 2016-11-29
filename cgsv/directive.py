from docutils import nodes
from docutils.parsers.rst import Directive as BaseDirective
from docutils.statemachine import ViewList
from sphinx.util import nested_parse_with_titles


class Directive(BaseDirective):

    def _parse(self, rst_text, annotation):
        result = ViewList()
        for line in rst_text.split("\n"):
            result.append(line, annotation)
        node = nodes.paragraph()
        node.document = self.state.document
        nested_parse_with_titles(self.state, result, node)
        return node.children

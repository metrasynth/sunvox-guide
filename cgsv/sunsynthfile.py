from docutils.parsers.rst import Directive


class SunsynthFileDirective(Directive):

    has_content = True

    def run(self):
        print(self.options)
        print(self.content)
        return []

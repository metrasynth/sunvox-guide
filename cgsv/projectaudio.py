from docutils.parsers.rst import Directive


class ProjectAudioDirective(Directive):

    has_content = True

    def run(self):
        print(self)
        print(self.state.document['source'])
        print(self.arguments)
        print(self.options)
        print(self.content)
        print()
        return []

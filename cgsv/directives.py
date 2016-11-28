from .connection import ConnectionDirective
from .module import ModuleDirective
from .modulegraph import ModuleGraphDirective
from .pattern import PatternDirective
from .patterntable import PatternTableDirective
from .project import ProjectDirective
from .projectaudio import ProjectAudioDirective
from .sunsynthfile import SunsynthFileDirective
from .sunvoxfile import SunvoxFileDirective


def setup(app):
    app.add_directive('svconnection', ConnectionDirective)
    app.add_directive('svmodule', ModuleDirective)
    app.add_directive('svmodulegraph', ModuleGraphDirective)
    app.add_directive('svpattern', PatternDirective)
    app.add_directive('svpatterntable', PatternTableDirective)
    app.add_directive('svproject', ProjectDirective)
    app.add_directive('svprojectaudio', ProjectAudioDirective)
    app.add_directive('sunsynthfile', SunsynthFileDirective)
    app.add_directive('sunvoxfile', SunvoxFileDirective)

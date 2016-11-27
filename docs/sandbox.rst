=======
Sandbox
=======

..  project:: sandbox
    :name: Sandbox Project

..  module:: sandbox.gen
    :type: Generator

..  connection:: sandbox
    :source: gen
    :dest: output

..  pattern:: sandbox.pat
    :pos: 0, 0
    :map: 1C=gen

    NNVVMMCCEEXXYY
    C4  1C        = Everything over here is commentary.
    //            - The = and - are for visual reference in the source code.
    //            - None of it is rendered in the final document.
    F4  1C        -
    //            = Note the use of mapping module "1C" to the "gen" module.
    //            - That maps the 1C in this pattern to the actual module.
    ==            -
    ..            -

Here's the complete module layout for the project:

..  graph:: project
    :style: basic

Here's just the generator module:

..  graph:: project.gen
    :style: detailed
    :depth: 0

Here's the pattern that we'll play:

..  patterntable:: project.pat
    :style: full

Take a listen:

..  audio:: sandbox
    :start: 0
    :duration: 3
    :fadeout: 1

Finally, download a copy of the project or the synth:

..  sunvoxfile:: sandbox
    :layout: auto

..  sunsynthfile:: sandbox.gen

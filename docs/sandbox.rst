=======
Sandbox
=======

..  svproject:: sandbox
    :name: Sandbox Project

..  svmodule:: sandbox.gen
    :type: Generator

    waveform = square
    attack = 20
    release = 20

..  svconnection:: sandbox
    :source: gen
    :dest: output

..  svpattern:: sandbox.pat
    :pos: 0, 0
    :map: 1C=gen

    NNVVMMCCEEXXYY  NNEEXXYY  NNVVMM
    C4  1C                    ==      * Everything over here is commentary.
    //                        ..      - The = and - are for visual reference in the source code.
    SP  1C    12FE            G4201C  - None of it is rendered in the final document.
    F4  1C                    //      -
    //    0001000F  <<08070B  ==      * Note the use of mapping module "1C" to the "gen" module.
    //    0001000F  <<08070B  ..      - That maps the 1C in this pattern to the actual module.
    ==                        C5201C  -
    ..                        //      -

Here's the complete module layout for the project:

..  svmodulegraph:: project
    :style: basic

Here's just the generator module:

..  svmodulegraph:: project.gen
    :style: detailed
    :depth: 0

Here's the pattern that we'll play:

..  svpatterntable:: project.pat
    :style: full

Take a listen:

..  svprojectaudio:: sandbox
    :start: 0
    :duration: 3
    :fadeout: 1

Finally, download a copy of the project or the synth:

..  sunvoxfile:: sandbox
    :layout: auto

..  sunsynthfile:: sandbox.gen

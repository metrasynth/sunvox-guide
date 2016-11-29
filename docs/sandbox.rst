=======
Sandbox
=======

..  svproject:: sandbox
    :name: My Sandbox Project

..  svmodule:: sandbox.gen
    :type: Generator
    :name: Square Wave Blip

    waveform = square
    attack = 20
    release = 20

..  svconnection:: sandbox
    :source: gen
    :dest: output

..  svpattern:: sandbox.pat
    :pos: 0, 0
    :map: 1C=gen

    NN VV MM CC EE XXYY | NN EE XXYY | NN VV MM
    C4    1C            |            | ==        * Everything over here is commentary.
    //                  |            | ..        - The = and - are for visual reference in the source code.
    SP    1C       12FE |            | G4 20 1C  - None of it is rendered in the final document.
    F4    1C            |            | //        -
    //       00 01 000F | << 08 070B | ==        * Note the use of mapping module "1C" to the "gen" module.
    //       00 01 000F | << 08 070B | ..        - That maps the 1C in this pattern to the actual module.
    ==                  |            | C5 20 1C  -
    ..                  |            | //        -

Here's the complete module layout for the project:

..  svmodulegraph:: sandbox
    :style: basic

Here's just the generator module:

..  svmodulegraph:: sandbox.gen
    :style: detailed
    :depth: 0

Here's the pattern that we'll play:

..  svpatterntable:: sandbox.pat
    :style: full

Take a listen:

..  svprojectaudio:: sandbox
    :start: 0
    :duration: 3
    :fadeout: 1

Finally, download a copy of the project or the synth:

..  sunvoxfile:: sandbox
    :layout: auto
    :filename: project1

..  sunsynthfile:: sandbox.gen
    :filename: synth1

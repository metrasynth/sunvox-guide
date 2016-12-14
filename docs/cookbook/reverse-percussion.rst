==================
Reverse Percussion
==================

..  svproject:: revkick
    :name: Reverse Kick Project
    :filename: reverse-percussion-revkick

..  svmodule:: revkick.*

Reversing percussion sounds can add uniqueness to a driving beat,
such as around phrase transitions, or to add an element of surprise
in the middle of a phrase.

Kick Drums
==========

One particular style of reversing kicks sounds kind of like a "whip",
as demonstrated by the very end of this phrase transition in
`SP23's "Leave This City Kickin" <https://sp23.bandcamp.com/album/leave-this-city-kickin>`__:

:download:`Download Reverse Kick Demonstration <reverse-percussion-sp23-leave-this-city-kickin-reverse-kick-sample.wav>`

This recipe shows you a way you can take a synth module,
then use the ping-pong setting of a loop module to create an isolated reversal.

..  svprojectaudio:: revkick
    :filename: reverse-percussion
    :start: 0
    :duration: 10
    :fadeout: 2

..  sunvoxfile:: revkick
    :filename: project

Modules
-------

kicker
  Provides a constant kick drum rhythm.

kick amp
  Turned on when we want to hear the forward kick drum,
  off when we want to reverse.

kick loop
  Provides a constant ping-pong loop of the kicker.

kick loop amp
  Turned off normally, and momentarily turned on to reveal
  the reverse portion of the ping-pong loop.

drumsynth
  Hi-hat and snare to fill out the rhythm.

..  svmodulegraph:: revkick
    :style: full

Patterns
--------

..  svpattern:: revkick.*

kick
....

Provides a constant kick drum rhythm via the kicker module.
This pattern is repeated throughout the example.

`kick on`_ and `kick off`_ control the presence of the kicker
via the kick amp module.

..  svpatterntable:: revkick.kick

perc
....

Hi-hat and snare to fill out the rhythm.

..  svpatterntable:: revkick.perc

perc halt
.........

A variation of perc_ to give room for the reverse kick.

..  svpatterntable:: revkick.perc_halt

kick on
.......

Turns on the kick amp, and resets the envelope acceleration of the kicker.

..  svpatterntable:: revkick.kick_on

kick off
........

Turns off the kick amp.

..  svpatterntable:: revkick.kick_off

kick loop
.........

Controls the reverse kick loop, and modifies the envelope acceleration of
the kicker so that the reversed kick sounds a little different than
the forward kick that plays immediately after.

..  svpatterntable:: revkick.kick_loop

----

..  rubric:: Contributors to this page

Author(s)
  Matthew Scott

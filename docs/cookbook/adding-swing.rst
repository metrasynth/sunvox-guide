============================
Adding swing to your project
============================

*Swing*, also known as shuffle or groove,
refers to stretching and shortening alternating notes of a rhythm.
It's often used to add a more relaxed feel to a song.

This recipe will focus on adding swing to 16th notes,
using the default 4/4 time and 16th note grid in SunVox.
We'll cover two ways to add swing,
and list the benefits and drawbacks of each method.


Common principles
=================

PPQN: Parts per quarter note
----------------------------

By default, lines in SunVox represent 16th notes.
Also by default, each line is divided into six ticks.
This means each quarter note is divided into 24 ticks,
or *24 PPQN (parts per quarter note)*.

24 PPQN is the default in SunVox for historical and practical reasons.
However, this gives you a limited range of swing amounts.

For adding more subtle swing to your project, 96 PPQN is useful.
Thankfully, SunVox supports this by changing the BPM and TPL
in project properties.

One way of doing this, while keeping 16th note lines in your patterns,
is to multiply both BPM and TPL in your project properties by 4.

The example project used here has an actual BPM of 80,
so the project's BPM is set to 320 and the TPL is set to 12.

Swing percentages
-----------------

Swing is often referred to as a percentage between 50% and 75%.
If an 8th note of time in a track represents 100%, the swing percentage
is the amount of time the first 16th note will occupy.
The second 16th note is then triggered and occupies the remainder.

Without adding any swing, your swing is at *50%*.
This means that both 16th notes are the same length::

               11111111112222222222333333333344444444
     012345678901234567890123456789012345678901234567   <-- tick (96 PPQN)
    +-----------------------><-----------------------+
    |<-50%------------------><-50%------------------>|  <-- 8th note divided into
    |<-24 ticks-------------><-24 ticks------------->|      equal 16th notes
    +-----------------------><-----------------------+
     \__________/\__________/\__________/\__________/   <-- 32nd notes
     0.......................1.......................   <-- line (16th note)

If we have a swing of *75%*, what effectively happens
is that the first 16th note becomes dotted (which means
it takes up 1.5 times the space of a 16th note)
and the second becomes a 32nd note::

               11111111112222222222333333333344444444
     012345678901234567890123456789012345678901234567
    +-----------------------------------><-----------+
    |<-75%------------------------------><-25%------>|
    |<-36 ticks-------------------------><-12 ticks->|
    +-----------------------------------><-----------+
     \__________/\__________/\__________/\__________/
     0.......................1.......................

This creates a very extreme swing, so typically something
in between is used, such as 62.5%, sometimes shown as "62%"
on hardware sequencers::

               11111111112222222222333333333344444444
     012345678901234567890123456789012345678901234567
    +-----------------------------><-----------------+
    |<-62.5%----------------------><-37.5%---------->|
    |<-30 ticks-------------------><-18 ticks------->|
    +-----------------------------><-----------------+
     \__________/\__________/\__________/\__________/
     0.......................1.......................

Now that you have knowledge of how swing works musically,
you can explore these methods for adding swing to your SunVox projects.


Example project without swing
=============================

..  svproject:: no-swing
    :name: No Swing Applied
    :filename: swing-shuffle-groove

..  svmodule:: no-swing.*

..  svpattern:: no-swing.*

As a point of comparison, here is what our example project sounds like before adding any swing.
In other words, its swing value is 50%.

..  svprojectaudio:: no-swing
    :filename: no-swing
    :start: 0
    :duration: 10
    :fadeout: 2

..  sunvoxfile:: no-swing
    :filename: no-swing

Modules
-------

We have a basic setup involving a FM synth passed through a couple of filters,
one of which has a line-based LFO running.
We also have a drum synth that's providing a kick, snare, and hihat.

..  svmodulegraph:: no-swing
    :style: detailed

FM pattern
----------

..  svpatterntable:: no-swing.fm

LFO initialization pattern
--------------------------

..  svpatterntable:: no-swing.lfo-reset

DrumSynth pattern
-----------------

..  svpatterntable:: no-swing.drums


Method 1: Global swing by setting TPL
=====================================

..  svproject:: method-1
    :name: Method 1, 96 PPQN, 56% swing
    :filename: swing-shuffle-groove-method1

..  svmodule:: method-1.*

..  svpattern:: method-1.*

This method works by alternating the number of ticks each line takes.
The first line sets it to the longer value, and the second line sets it to the shorter.

It will affect all notes in all patterns globally,
and you will also see the swing visually during playback.

Applying the method
-------------------

Find the "1st note ticks" and "2nd note ticks" that match your PPQN and desired swing amount.
(See Tables_)

Create a new pattern that alternates between the two values using the
:doc:`/note-effects/0f-set-playing-speed` note effect.

Clone the pattern as many times as needed to reach the end of your song
(or the end of the section where you want swing).

Here's what it looks like to apply 56% swing:

..  svpatterntable:: method-1.swing

Here's what it sounds like:

..  svprojectaudio:: method-1
    :filename: method-1
    :start: 0
    :duration: 10
    :fadeout: 2

..  sunvoxfile:: method-1
    :filename: method-1

Notice how the filter's LFO no longer aligns the same way as before.
This is one of the side-effects of this method and is discussed in the list of drawbacks below.

Advantages
----------

- Requires only a single track to apply swing to all notes.

- Swing across entire project can be adjusted quickly.

- All note effects may be used.

Drawbacks
---------

* All tracks must follow the same swing amount.
  Track-specific swing, as described below, can allow for this.
  Mixing the two techniques is left as an exercise for the reader.

* Maximum swing value is 64% when using 96 PPQN, as TPL cannot be set past 31.

* If you have any LFOs set to use "line", "line/2", or "line/3" as a frequency unit,
  they will be affected by the shifting TPL.
  You may hear audible clicks as a result.
  Use a different frequency unit, or try track-specific swing instead.
  Affected modules:
  :doc:`/modules/effects/delay`,
  :doc:`/modules/effects/echo`,
  :doc:`/modules/effects/filter`,
  :doc:`/modules/effects/filterpro`,
  :doc:`/modules/effects/flanger`,
  :doc:`/modules/effects/lfo`,
  :doc:`/modules/effects/vibrato`.


Method 2: Track-specific swing by delaying notes
================================================

..  svproject:: method-2
    :name: Method 2, 96 PPQN, variable swing
    :filename: swing-shuffle-groove-method2

..  svmodule:: method-2.*

..  svpattern:: method-2.*

This method works by alternating the number of ticks each line takes.
The first line sets it to the longer value, and the second line sets it to the shorter.

It will affect all notes in all patterns globally,
and you will also see the swing visually during playback.

Applying the method
-------------------

Find the "2nd note delay" that matches your PPQN and desired swing amount.
(See Tables_)

Delay every second line in the sequence of notes you want to swing using the
:doc:`/note-effects/1d-delay-start-during-line` note effect.

Here's what it looks like to apply 56% swing to our FM bassline,
52% to our kick drum, 62% to our hihats, and 75% to our snare:

..  svpatterntable:: method-2.fm

..  svpatterntable:: method-2.drums

Here's what it sounds like:

..  svprojectaudio:: method-2
    :filename: method-2
    :start: 0
    :duration: 10
    :fadeout: 2

..  sunvoxfile:: method-2
    :filename: method-2

This example may be a bit overdone,
but it shows how you can use different swing values simultaneously.

The filter's LFO aligns the same way as without swing, because we are not changing the size of lines.

Advantages
----------

- Simpler way to have different swing amounts for different tracks.

- LFOs using "line", "line/2", or "line/3" as a frquency unit will not be affected as the TPL will stay fixed.

Drawbacks
---------

- Must place note effects in an adjacent track.

- More difficult to change swing values once set.

- Some note effects may not be used:
  20-23 (random notes and controller values),
  40-5f (delay event for line fraction).


Tables
======

Here is a table of swing percentage values.
It'll be useful for the techniques explained below.
Each value shows the number of ticks each 16th note will take,
and the number of ticks the second 16th note will need to be delayed.

If you're using a TPL other than 6, 12, or 24, I applaud you for your creativity!
You'll have to calculate swing and BPM on your own,
but the same methods described above will still apply.

24 PPQN
-------

Keep TPL at 6.

====  ==============  ==============  ==============
%     1st note ticks  2nd note ticks  2nd note delay
====  ==============  ==============  ==============
50    6               6               0
58    7               5               1
66    8               4               2
75    9               3               3
====  ==============  ==============  ==============

48 PPQN
-------

Set TPL to 12, multiply project BPM by 2.

====  ==============  ==============  ==============
%     1st note ticks  2nd note ticks  2nd note delay
====  ==============  ==============  ==============
50    12 (c)          12 (c)          0  (0)
54    13 (d)          11 (b)          2  (2)
58    14 (e)          10 (a)          4  (4)
62    15 (f)          9  (9)          6  (6)
66    16 (10)         8  (8)          8  (8)
70    17 (11)         7  (7)          10 (a)
75    18 (12)         6  (6)          12 (c)
====  ==============  ==============  ==============

96 PPQN
-------

Set TPL to 24, multiply project BPM by 4.

..  note::

    Maximum TPL is 31, so 64% swing is highest available using
    `Method 1: Global swing by setting TPL`_.

====  ==============  ==============  ==============
%     1st note ticks  2nd note ticks  2nd note delay
====  ==============  ==============  ==============
50    24 (18)         24 (18)         0  (0)
52    25 (19)         23 (17)         1  (1)
54    26 (1a)         22 (16)         2  (2)
56    27 (1b)         21 (15)         3  (3)
58    28 (1c)         20 (14)         4  (4)
60    29 (1d)         19 (13)         5  (5)
62    30 (1e)         18 (12)         6  (6)
64    31 (1f)         17 (11)         7  (7)
66                                    8  (8)
68                                    9  (9)
70                                    10 (a)
72                                    11 (b)
75                                    12 (c)
====  ==============  ==============  ==============


Further reading
===============

For more about the history behind swing and quantization,
read this `interview with Roger Linn`_,
creator of the LinnDrum drum machine and designer of early Akai MPC workstations.

..  _interview with Roger Linn:
    https://www.attackmagazine.com/features/interview/roger-linn-swing-groove-magic-mpc-timing/


----

..  rubric:: Contributors to this page

Author(s)
  Matthew Scott

============================
Exporting to WAV files [WIP]
============================

Sunvox can render your music to a .WAV file so that you can copy it, add it to
other mixes, transcode it or whatever else you want to do.

Select the main menu in the upper left hand corner, then choose Export/import.
This should open a little box with two options:

* Export to WAV
* Export to MIDI

What we want here is to export to WAV, so select that one.

This opens another window called Select export format.

You can choose your bit depth. There are two options: 16 bit (integer) and
32 bit (floating point). If you don't know which to choose, 16 bit is not
going to get you in any trouble. That's CD quality. 32 bit is overkill
for most purposes.

You can also choose your export mode:

* One file (Output)
* One file (selected module)
* File per module
* File per module (effects)
* File per module (connected to Output)

If you just want to hear your song, choose One file (Output).

Next click the Export button. This will open a window in which you can name
your file, and sunvox will render your file for you. Once this is done, you
can copy it, listen to it - whatever you like!

The other export modes meet other needs, and are a little more advanced.

One file (selected module) lets you just get the sound that came from one
module in your song, rather than just all the sound that emerged from Output.

File per module is kind of like selected module, except that it will generate
a separate WAV file for every single module. Careful, on a big project this
can take a lot of storage! Each filename will start with a name that you gave,
then the module's number, then the module type, for example:

    MySong_01_Generator.wav

File per module (effects) is like file per module, but only creates the output
of each effects module. This can make sense if you're only interested in the
post-effects output of every sound, rather than saving the raw sounds as well.

File per module (connected to Output) lets you save the output of every module
that is linked to the Output module. This can make a lot of sense if you want
the final sounds that reached the Output module, but you want them broken out.

In general, the other options are for musicians who want to extract stems from
a sunvox song so that they can apply another stage of mastering. If you use
sunvox as your end-to-end musical solution, you probably won't need these.
Just save one file, from Output, and show the world your music.

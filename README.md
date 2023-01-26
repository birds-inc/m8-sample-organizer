**[Click here to download!](https://github.com/birds-inc/m8-sample-organizer/archive/refs/heads/main.zip)**

This is a Python script to organize and convert your samples for the M8 tracker.  You'll run this tool on the command-line - instructions below.

**[Watch a video on how to use this tool](https://www.youtube.com/watch?v=VI0IuEDY8HI).**

# M8 Sample Organizer

The [M8 is a delightful, gameboy-shaped sampler, sequencer and synthesizer](https://dirtywave.com/).

But if you've ever tried loading your sample library on it, you've probably run into problems:

* Many samples **don't load or play correctly**
* Folder and file names are **too long**
* **Navigating** layers of folders is tedious

**M8 Sample Organizer** cleans it up!  It turns samples from your library like this:

* `Capsun - Lo-Fi Soul & Future Beats`
* / `CPA_CAPSUN_Lo_Fi_Soul___Future_Beats`
* / `Drums___Percussion`
* / `Drum___Perc_One_Shots`
* / `Snare`
* / `CLF_Snare_Chunk.wav`

into:

* `Capsun_Lo_Fi_Soul_&_Future_Beats`
* / `Drums_Percussion_Perc_One_Shots_Snare`
* / `CLF_Snare_Chunk.wav`

It does lots of cleanup:

* **Converts** audio files to M8-approved 16-bit WAV files
* **Removes** duplicate words, punctuation and common filler phrases (like `processed` and `final`)
* **Simplifies** layers of folders into one level
* **Detects** new files added to your library each time you run it

# Instructions

This is a command-line tool, so you'll need to open a Terminal or cmd.exe shell to run it.

## Install Python

Python is pre-installed on most computers - try the command `python --version` or `python3 --version` to see if it exists.

Otherwise, you can install it from [Python.org](https://www.python.org/downloads/).  Note the installation path for later reference.

## Install FFmpeg

[FFmpeg](https://ffmpeg.org/download.html) is a free, industry-standard tool used to convert and format audio files for use on the M8.

Note the installation path for later reference.

## Download the M8 Sample Organizer

**[Click here](https://github.com/birds-inc/m8-sample-organizer/archive/refs/heads/main.zip)** to download the **M8 Sample Organizer** code.  Unzip the contents.

## Set up the config file

In the M8 Sample Organizer folder, there's a file called `config.yml-sample`.  Rename this file to `config.yml`.

Then edit the `SRC_FOLDER`, `DEST_FOLDER`, and `FFMPEG_PATH` to point at your audio library and FFmpeg.  `DEST_FOLDER` is where this tool will create files, so be sure to set it someplace safe!

You can also configure any additional cleanup settings to your liking, add new strike words, etc.

## Install yaml

We need a Python library for reading the configuration file - install it by running this command:

`python3 -m pip install pyyaml`

(If `python3` fails, try just `python` instead.)

## Run the tool

Finally, navigate to the `m8-sample-organizer-main` folder and run the following command:

`python3 src/m8-sample-organizer.py`

That's it!  You'll see as it begins to copy and convert your sample library.

As you add more samples to your library, you can rerun this tool - by default, any existing files will be ignored, so only new ones will be processed.

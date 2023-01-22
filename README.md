# M8 Sample Organizer

The [M8 is a portable tracker sequencer and synthesizer](https://dirtywave.com/) with rich sample support.

If you've ever tried loading your sample library on the M8's SD card, you'll notice there are several problems:

* Many samples **don't load or play correctly**
* Folder and file names are **too long**
* **Navigating** layers of folders is tedious

**M8 Sample Organizer** cleans it up!  It turns samples like this:

`Capsun - Lo-Fi Soul & Future Beats` / `CPA_CAPSUN_Lo_Fi_Soul___Future_Beats` / `Drums___Percussion` / `Drum___Perc_One_Shots` / `Snare` / `CLF_Snare_Chunk.wav`

into:

`Capsun_Lo_Fi_Soul_&_Future_Beats` / `Drums_Percussion_Perc_One_Shots_Snare` / `CLF_Snare_Chunk.wav`

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

[Click here](https://github.com/birds-inc/m8-sample-organizer/archive/refs/heads/main.zip) to download the **M8 Sample Organizer** code.  Unzip the contents.

## Set up the config file

In the M8 Sample Organizer folder, there's a file called `config.yml-sample`.  Rename this file to `config.yml`.

Then edit the file accordingly - change the path to your sample library and FFmpeg, and configure any additional cleanup settings to your liking.

## Run the tool

Finally, run the following command:

`python src/m8-sample-organizer.py`

You'll see as it begins to copy and convert your sample library.

By default, any existing files will be ignored, so this tool is safe to rerun as you add more samples to your library.

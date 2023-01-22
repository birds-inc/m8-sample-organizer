# M8 Sample Organizer

The [M8 is a portable tracker sequencer and synthesizer](https://dirtywave.com/), with rich sample support.

But if you've ever tried loading your sample library on the M8's SD card, you'll notice there are several problems:

* Many samples **don't load or play correctly**
* Folder and file names are **too long**
* **Navigating** layers of folders is tedious

**M8 Sample Organizer** fixes this!  Just point it at your sample library and specify a destination folder, and it will:

* **Clean up and shorten** long folder and filenames
* **Convert** your audio files into M8-approved 16-bit WAV files
* **Detect** and copy new files over as they're added to your library

For example, let's say your library includes this path:

* `Capsun - Lo-Fi Soul & Future Beats` / `CPA_CAPSUN_Lo_Fi_Soul___Future_Beats` / `Drums___Percussion` / `Drum___Perc_One_Shots` / `Snare` / `CLF_Snare_Chunk.wav`

This would be shorted and simplified to:

* `Capsun_Lo_Fi_Soul_&_Future_Beats` / `Drums_Percussion_Perc_One_Shots_Snare` / `CLF_Snare_Chunk.wav`

All the duplicate words have been removed, layers of folders collapsed to one level, and excess punctuation and filler words removed!

# Instructions

This is a command-line tool, so you'll need to open a Terminal or cmd.exe shell to run it.

## Install Python

Python is pre-installed on most computers - try the command `python --version` or `python3 --version` to see if it exists.

Otherwise, you can install it from [Python](https://www.python.org/downloads/).  Note the installation path for later reference.

## Install FFmpeg

[FFmpeg](https://ffmpeg.org/download.html) is a free, open-sourced tool used to correctly convert and format audio files for use on the M8.

Note the installation path for later reference.

## Download the M8 Sample Organizer

[Click here](https://github.com/birds-inc/m8-sample-organizer/archive/refs/heads/main.zip) to download the **M8 Sample Organizer** code.  Unzip the contents.

## Set up the config file

In the M8 Sample Organizer folder, there's a file called `config.yml-sample`.  Rename this file to `config.yml`.

Then edit the file a

1. install ffmpeg
1. modify constants
1. run `make local`

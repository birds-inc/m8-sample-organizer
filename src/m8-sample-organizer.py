import os
import re
import string
import subprocess
import wave
import scipy.io.wavfile as wavfile
import yaml


with open("config.yml", "r") as f:
    config = yaml.safe_load(f)


SRC_FOLDER = config["SRC_FOLDER"]
DEST_FOLDER = config["DEST_FOLDER"]
FFMPEG_PATH = config["FFMPEG_PATH"]
TARGET_BIT_DEPTH = config["TARGET_BIT_DEPTH"]
FILE_TYPES = config["FILE_TYPES"]
SPLIT_PUNCTUATION = config["SPLIT_PUNCTUATION"]
FILL_PUNCTUATION = config["FILL_PUNCTUATION"]
STRIKE_WORDS = [word.lower() for word in config["STRIKE_WORDS"]]
JOIN_SEP = config["JOIN_SEP"]
SKIP_EXISTING = config["SKIP_EXISTING"]


def get_files_by_type(folder, file_types=None):
    # Initialize an empty list to store the file paths
    file_paths = []

    # Iterate through the files in the folder
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file_types:
                # Get the file extension
                file_ext = file.split(".")[-1]
                # If the file extension is in the list of file types, add the file path to the list
                if file_ext not in file_types:
                    continue

            file_path = os.path.join(root, file)
            file_paths.append(file_path)

    return file_paths

def strip_path_prefix(path, prefix):
    # Ensure that the prefix ends with a separator
    if not prefix.endswith(os.sep):
        prefix = prefix + os.sep

    # Check if the path starts with the prefix
    if path.startswith(prefix):
        # Strip the prefix from the path and return the remainder
        return path[len(prefix):]
    else:
        # Return the original path if it doesn't start with the prefix
        return path

def shorten_path(path):
    # Clean up the punctuation
    for c in SPLIT_PUNCTUATION:
        path = path.replace(c, " ")

    for c in FILL_PUNCTUATION:
        path = path.replace(c, "")

    # Split the path into a list of parts (i.e., folders)
    parts = path.split(os.sep)

    pack = parts[0]
    path = parts[1:-1]
    file = parts[-1]

    # Create a set to store the unique words
    unique_words = set()

    pack = clean_folder(pack, unique_words)
    path = clean_path(path, unique_words)
    file = clean_file(file, unique_words)
    
    # Join the parts back together
    parts = [pack, path, file]
    path = os.sep.join([part for part in parts if part])

    return path

def clean_folder(folder, unique_words):
    words = folder.split()

    words = remove_dupe_words(words, unique_words)
    
    words = [capitalize(word) for word in words]

    pack = JOIN_SEP.join(words)

    return pack
    
def clean_path(path, unique_words):
    for i, folder in enumerate(path):
        path[i] = clean_folder(folder, unique_words)

    path = [folder for folder in path if folder]

    return JOIN_SEP.join(path)

def clean_file(file, unique_words):
    parts = file.split(".")

    extension = parts[-1]

    filename = " ".join(parts)

    words = filename.split()

    words = [capitalize(word) for word in words]

    file = JOIN_SEP.join(words[:-1]) + "." + extension
    
    return file

def remove_dupe_words(words, unique_words):
    # Remove duplicate words
    words = [word for word in words if word.lower() not in unique_words]

    # Remove any strike words
    words = [word for word in words if not any(word.lower().startswith(prefix) for prefix in STRIKE_WORDS)]

    # Add the remaining words to the set of unique words
    unique_words.update([word.lower() for word in words])

    # Flip the plurals and add those to our set of unique words
    flipped_plurals = []
    for word in words:
        if word.endswith('s'):
            flipped_plurals.append(word[:-1])
        else:
            flipped_plurals.append(word + 's')

    unique_words.update([word.lower() for word in flipped_plurals])

    return words

def capitalize(word):
    if word[0].islower():
        word = word[0].upper() + word[1:]
    return word

def convert_wav_to_16bit(ffmpeg_path, input_path, output_path):
    # Create the directories in the output path if they do not exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Construct the FFmpeg command
    command = [ffmpeg_path, '-hide_banner', '-loglevel', 'error', '-y', '-i', input_path, '-acodec', 'pcm_s16le', output_path]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print("error converting!")

def main():
    files = get_files_by_type(SRC_FOLDER, file_types=FILE_TYPES)

    for src_path in files:
        relative_path = strip_path_prefix(src_path, SRC_FOLDER)
        short_path = shorten_path(relative_path)
        dest_path = os.path.join(DEST_FOLDER, short_path)

        if SKIP_EXISTING and os.path.exists(dest_path):
            continue

        print("Input  {}".format(relative_path))
        print("Output {}".format(short_path))
        print()

        convert_wav_to_16bit(FFMPEG_PATH, src_path, dest_path)

    print("{} files processed.".format(len(files)))

main()

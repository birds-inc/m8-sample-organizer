import os
import re
import string

SRC_FOLDER = os.path.join(
    os.path.expanduser("~"),
    "Documents", "Splice", "Samples", "packs"
)
DEST_FOLDER = os.path.join(
    os.path.expanduser("~"), "Documents", "m8 samples"
)

FILE_TYPES = ["wav"]
PUNCTUATION = ["_", " ", "-", "+"]

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
    for c in PUNCTUATION:
        path = path.replace(c, " ")

    # Split the path into a list of parts (i.e., folders)
    parts = path.split(os.sep)

    # Create a set to store the unique words
    unique_words = set()

    # Apply the function to each part
    for i, part in enumerate(parts[:-1]):
        # Split the part into words
        words = part.split()

        # Remove duplicate words
        words = [word for word in words if word not in unique_words]

        # Add the remaining words to the set of unique words
        unique_words.update(words)

        # Flip the plurals and add those to our set of unique words
        flipped_plurals = []
        for word in words:
            if word.endswith('s'):
                flipped_plurals.append(word[:-1])
            else:
                flipped_plurals.append(word + 's')
        unique_words.update(flipped_plurals)

        # Capitalize all words
        words = [capitalize(word) for word in words]

        # Join the words back together and update the part
        parts[i] = "".join(words)

    # Modify the filename
    words = parts[-1].split()
    words = [capitalize(word) for word in words]
    parts[-1] = "".join(words)

    # Join the parts back together
    path = os.sep.join([part for part in parts if part])

    return path

def capitalize(word):
    if word[0].islower():
        word = word[0].upper() + word[1:]
    return word


def main():
    for file in get_files_by_type(SRC_FOLDER, file_types=FILE_TYPES):
        full_path = file
        relative_path = strip_path_prefix(full_path, SRC_FOLDER)

        short_path = shorten_path(relative_path)
        print(short_path)

main()

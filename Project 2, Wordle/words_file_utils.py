"""
Words file utility functions.

Author: WILLIAM JEDRZEJCZAK
Version: 11/6/2023
"""


def process_word_file(filename):
    """
    Read the file, check its correctness, and.

    return the word collection name and its data
    This file has the following format: The first line must
    contain the word WORDS
    followed by a space, and the rest of the first line is
    interpreted as the name
    for this collection of words. The following lines in the
    file can be in any format,
    for example:
        WORDS War and Peace
        ...
        the text of the book War and Peace
        ...

    If any of the following errors occur, the function
    should return None:
    - The file does not have "WORDS" as the first word on the first line
    - The file does not contain a name for the word collection on the 1st line
    - The rest of the file is empty

    If there are no errors, the function should return a tuple of 2 items:
    - The name of the word collection in a single string
    - The word collection in a single string

    Args:
        filename (str): The name of the file to read from

    Returns:
        tuple: A tuple containing the name of the word collection
               and its data as a single string or
               None if any of the errors occur.
    """
    try:
        with open(filename, 'r') as file:
            first_line = file.readline().strip()
            if first_line.startswith("WORDS "):
                collection_title = first_line[6:]
            else:
                return None
            text = file.read()
            if not collection_title:
                return None
            if not text.strip():
                return None
            return (collection_title, text)
    except FileNotFoundError:
        return None

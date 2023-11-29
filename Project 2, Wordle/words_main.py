"""Words - a game based on Wordle.

Author: Will and CS149 Faculty
Version: 11/14/2023
"""

import os
import sys
import colorama
import nltk
from words_utils import clean_word_set, categorize_words, collect_unique_words
from words_file_utils import process_word_file
import words_game


def process_args(argv):
    """Process the command-line arguments.

    Check for the correct number of args. Print the usage \
    statement & then return None if incorrect.
    For each file:
        - If a file does not exist (according to the os module) just\
        skip it with no messages.
        - Use the process_word_file function to make sure each file\
        has the right format and read its text.
        - If a file has the wrong format or no text, just skip it\
        with no messages.
        - Use the collect_unique_words function to process the \
        file's text into a set of unique words.
        - Use the clean_word_set function to process the unique \
        word set into a list of valid words.
        - If there are any words left, use the categorize_words \
        function to put them into a dictionary
        organized by lengths (key is length) and add that dictionary \
        and the word collection title
        to a list of tuples.
    Return the list of tuples - 1 tuple per file that has no errors
    and contains valid words.

    Args:
        argv (list): the list of command line arguments

    Returns:
        list: a list of tuples, where each tuple contains a
        str (title of collection),
                and a dict (of the words from the collection)
    """
    if len(argv) < 2:
        print("Usage: python words_main.py collection_title_1 \
collection_file_1 ...")
        return None
    collections = []
    for text in argv:
        if os.path.exists(text):
            text = process_word_file(text)
            if text is not None:
                unique_words = collect_unique_words(text[1])
                valid_words = clean_word_set(unique_words)
                if len(valid_words) > 0:
                    word_dict = categorize_words(valid_words)
                    collections.append((text[0], word_dict))

    return collections


if __name__ == "__main__":
    colorama.init(autoreset=True)

    # Load the nltk wordnet data
    nltk.download('wordnet')

    word_dicts = process_args(sys.argv)
    if word_dicts is None:
        sys.exit(1)

    if len(word_dicts) > 0:
        words_game.play_words_game(word_dicts)
    else:
        print("No legal words in these collections.")

"""Utility functions for word collections.

Author: WILLIAM JEDRZEJCZAK
Version: 11/2/2023
"""
from words_game_utils import is_valid_word
import nltk
nltk.download('words')


def check_letters(word):
    """Check each letter in a word to make sure it is in the English alphabet.

    It turns out s.isalpha() accepts characters with umlauts and accent marks,
    which cannot easily be typed on an English keyboard.  Return True if the
    word contains only the letters 'A' through 'Z' and False otherwise.

    Args:
        word(str): the word to check

    Returns:
        bool: True if the word contains only English letters
    """
    return all(char.isalpha() and char.isascii()
               and char.isupper() for char in word)


def collect_unique_words(text):
    """Take the text string passed in and produce a set of unique words.

    Split the text into words
    Change every word to uppercase
    Remove common surrounding punctuation: ().,?!;:#-_'"
    Place the words into a set to remove duplicates, and return

    Args:
        text(str): The text to process

    Returns:
        set: set of unique words from the text
    """
    punctuation = ['(', ')', '.', ',', '?', '!',
                   ';', ':', '#', '-', '_', "'", '"']

    individual_words = set()
    words = text.split()
    for word in words:
        for punk in punctuation:
            word = word.strip(punk)
        word = word.upper()
        individual_words.add(word)
    return individual_words


def clean_word_set(word_set):
    """
    Take a set of unique words and produce a set of legal words.

    Return a list of the words that have no duplicate letters
    and contain only letters
    And are considered valid words by nltk

    Args:
        word_set (set): A set of words

    Returns:
        list: List of legal words from the set, all made uppercase
    """
    valid_words = []
    for word in word_set:
        count = 0
        if check_letters(word):
            if is_valid_word(word):
                for letter in word:
                    if word.count(letter) != 1:
                        break
                    count += 1
                if count == len(word):
                    word = word.upper()
                    valid_words.append(word)
    return valid_words


def categorize_words(word_list):  # Completed
    """Take a list of legal unique words and categorized them.

    Produce a dictionary of the form {int:list}.
    is a list of words of that length, for example:
    {
     2: ['is', 'on', 'at'],
     5: ['value', 'legal', 'words', 'trail']
    }

    Args:
        word_list(list): a list of words

    Returns:
        dict: a dictionary categorized by word length
    """
    word_dict = {}
    for word in word_list:
        word_length = len(word)
        if word_length not in word_dict:
            word_dict[word_length] = [word]
        else:
            word_dict[word_length].append(word)
    return word_dict

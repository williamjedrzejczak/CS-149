"""
Words game utility functions.

Author: WILLIAM JEDRZEJCZAK
Version: 11/2/2023
"""
from nltk.corpus import wordnet
import random
from colorama import Fore
BULL = 2
COW = 1
WRONG = 0


def get_hint(word):  # Completed
    """Return a hint for this word.

    PART C: use nltk to get a definition for this word.

    Args:
        word (str): the word to find a definition for

    Returns:
        str: a definition or hint for this word
    """
    synsets = wordnet.synsets(word)
    if synsets:
        definition = synsets[0].definition()
        return definition
    else:
        return f"No definition found for '{word}'"


def is_valid_word(word):  # DONE LMFAO
    """Check that this word is not a proper noun and a real dictionary word.

    Args:
        word (str): the word to check

    Returns:
        bool: True if the word is valid, False otherwise
    """
    synsets = wordnet.synsets(word)
    return len(synsets) > 0


def get_random_word(word_dict, length):  # ALREADY DONE
    """Select a random word of the selected length.

    Args:
        word_dict (dict): a dict {int:list} where a key is a length,
            and the value is a list of words of that length
        length (int): the desired word length

    Returns:
        str: a random word from the word_dict's list for the given length
    """
    if length in word_dict:
        return random.choice(word_dict[length])
    else:
        return None


def check_guess(secret, guess):  # Done and Done Correctly.
    """Compare the user's guess to the secret word.

    If the guess is the wrong length return None
    Create an empty list, then for each letter in the guess:
        add a 0 (WRONG) if the letter is not in the secret word
        add a 1 (COW) if the letter is in the word but in the wrong position
        add a 2 (BULL) if the letter is in the correct position in the word

    Args:
        secret (str): the secret word being guessed
        guess (str): the current guess

    Returns:
        list: a list of testers, one for each letter
    """
    if len(secret) != len(guess):
        return None

    testers = [WRONG] * len(secret)
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            testers[i] = BULL
        elif guess[i] in secret:
            testers[i] = COW

    return testers


def color_string(result, guess):  # Done and Done Correctly.
    """Use a result list of letter testers and a guess, print the word.

    Color scheme:
        red if the letter is not in the secret word
        yellow if the letter is in the word but in the wrong position
        green if the letter is in the correct position in the word
    To assure the resulting string is readable to all users:
        surround green letters with square brackets []
        surround yellow letters with parentheses ()
        leave red letters as is
    For example:
        color_string([1, 0, 2, 1, 0], "PRINT") -> "(P)R[I](N)T"

    Args:
        result (str): the list of letter testers - 0, 1, 2
        guess (str): the current guess

    Returns:
        str: a string where each letter has the right color and is visually ma.
    """
    finalword = ""
    for i in range(len(guess)):
        if result[i] == BULL:
            finalword += f"{Fore.GREEN}[{guess[i]}]{Fore.RESET}"
        elif result[i] == COW:
            finalword += f"{Fore.YELLOW}({(guess[i])}){Fore.RESET}"
        elif result[i] == WRONG:
            finalword += f"{Fore.RED}{guess[i]}{Fore.RESET}"
        else:
            finalword += guess[i]
    return finalword


def collection_menu(word_dicts):  # Done and Done Correctly.
    """Create a single string of the word collection names for.

    COLLECTIONS
    1    collection_name_0
    2    collection_name_1
    ...
    n    collection_name_n

    Args:
        word_dicts (list): a list of tuples of type (str, dict): a name.

    Returns:
        str: a string with the given format
    """
    menu = "COLLECTIONS\n"
    for i, (collection_name, _) in enumerate(word_dicts, start=0):
        menu += f"{i}    {collection_name}\n"
    return menu

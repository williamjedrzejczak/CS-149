"""Words game testing words_game_utils functions.

Author: WILLIAM JEDRZEJCZAK
Version: 11/3/2023
"""
from words_game_utils import BULL, COW, WRONG, \
     check_guess, color_string, collection_menu, get_hint, is_valid_word
from colorama import Fore
import nltk

def test_check_guess():
    # Another Test
    secret = "WORD"
    guess = "WORD"
    result = check_guess(secret, guess)
    assert result == [BULL, BULL, BULL, BULL]
    # Another Test
    # Another Test
    secret = "WORD"
    guess = "WROD"
    result = check_guess(secret, guess)
    assert result == [BULL, COW, COW, BULL]
    # Another Test
    # Another Test
    secret = "WORD"
    guess = "TIGER"
    result = check_guess(secret, guess)
    assert result is None
    # Another Test
    # Another Test
    secret = ""
    guess = "TIGER"
    result = check_guess(secret, guess)
    assert result is None


def test_color_string():
    # Test w all letters are in the correct position (green brackets)
    assert color_string([BULL, BULL, BULL, BULL], "WORD") == f"{Fore.GREEN}\
[W]{Fore.RESET}{Fore.GREEN}[O]{Fore.RESET}{Fore.GREEN}[R]{Fore.RESET}\
{Fore.GREEN}[D]{Fore.RESET}"

    # Test w all letters are in the wrong position (yellow parentheses)
    assert color_string([COW, COW, COW, COW], "LOVE") == f"{Fore.YELLOW}\
(L){Fore.RESET}{Fore.YELLOW}(O){Fore.RESET}{Fore.YELLOW}(V){Fore.RESET}\
{Fore.YELLOW}(E){Fore.RESET}"

    # Test w all letters are not in word (red letters)
    assert color_string([WRONG, WRONG, WRONG, WRONG], "TEST") == f"\
{Fore.RED}T{Fore.RESET}{Fore.RED}E{Fore.RESET}{Fore.RED}S{Fore.RESET}\
{Fore.RED}T{Fore.RESET}"

    # Test w a mix of green, yellow, and red letters
    assert color_string([BULL, COW, WRONG, BULL, COW], "COLOR") == f"\
{Fore.GREEN}[C]{Fore.RESET}{Fore.YELLOW}(O){Fore.RESET}{Fore.RED}\
L{Fore.RESET}{Fore.GREEN}[O]{Fore.RESET}{Fore.YELLOW}(R){Fore.RESET}"


def test_collection_menu():
    # Testing w an empty list.
    assert collection_menu([]) == "COLLECTIONS\n"

    # Test w a singlular collection.
    assert collection_menu([("Collection 1", {})]) == "COLLECTI\
ONS\n0    Collection 1\n"

    # Test multiple collections.
    word_dicts = [
        ("Collection A", {}),
        ("Collection B", {}),
        ("Collection C", {}),
    ]
    expected_output = "COLLECTIONS\n0    Collection A\n1    Col\
lection B\n2    Collection C\n"
    assert collection_menu(word_dicts) == expected_output

    # Test collections w longer names.
    word_dicts = [
        ("Very Long Collection Name", {}),
        ("Short", {}),
        ("Another Long Collection Name", {}),
    ]
    expected_output = "COLLECTIONS\n0    Very Long Collecti\
on Name\n1    Short\n2    Another Long Collection Name\n"
    assert collection_menu(word_dicts) == expected_output

def test_get_hint():
    # Test a word with a definition
    hint = get_hint("apple")
    assert hint == "fruit with red or yellow or green skin and sweet to tart crisp whitish flesh"

    # Test a word with no definition
    hint = get_hint("zyxwvutsrqponmlkjihgfedcba")
    assert hint == "No definition found for 'zyxwvutsrqponmlkjihgfedcba'"
    

def test_is_valid_word():
    # Valid English words
    assert is_valid_word("apple") == True

    # Proper nouns and non-English words
    assert is_valid_word("computer") == False
    assert is_valid_word("12345") == False

    # Common abbreviations
    assert is_valid_word("lol") == False

    # Non-existent words
    assert is_valid_word("zygomatic") == True

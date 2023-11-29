"""Words - a game based on Wordle.

Author: CS149 Faculty
Version: 11/01/2023
"""

import words_game_utils as wgu


def ask_book_id(len):
    """Prompt for a book id.

    Args:
        len (int): desired word length

    Returns:
        int: the book id input by the user
    """
    val = input("Enter the id of the collection: ")
    while not val.isnumeric() or int(val) < 0 or int(val) >= len:
        val = input("Enter the id of the collection: ")
    return int(val)


def ask_length(lengths):
    """Prompt for a word length.

    Args:
        lengths (list): available word lengths

    Returns:
        int: word length input by the user
    """
    print(f'The word lengths available are: {lengths}')
    val = input("Enter the length of the word: ")
    while not val.isnumeric() or int(val) not in lengths:
        val = input("Enter the length of the word: ")
    return int(val)


def play_round(word):
    """Play a single round.

    Keep playing until the user guesses the code, or
    types a single 'q' or 'Q' as their guess to quit.

    Args:
        word(str): the word the user must guess
    """
    # Included for DEBUGGING
    print(f"The secret word is {word}")

    wlen = len(word)
    i = 0
    print(f'\nYou have {wlen+1} guesses.')
    print(f'Hint: {wgu.get_hint(word)}\n')

    while ((i <= wlen) and (guess := input(f"Enter your guess {i+1}: ").upper()) != 'Q'):
        if not wgu.is_valid_word(guess):
            print("Not a recognized word.")
            continue
        if (result := wgu.check_guess(word, guess)) is not None:
            print(wgu.color_string(result, guess))
            if result.count(wgu.BULL) == len(result):
                print('You guessed the word!\n')
                break
        else:
            print(f"Your guess must be length {wlen}.")
        i += 1
    print(f'The word was {word}\n')


def play_words_game(word_dicts):
    """Keep playing games until the user wants to stop.

    Ask the user if they want to play a game.  If they don't answer 'y' or 'Y', stop.
    Using the functions above, get the game mode information and play a single round.
    Go back and ask again.

    Args:
        word_dicts(list): a list of tuples of type (str, dict): a name and a word collection
    """
    while input("Do you want to play [y/Y]: ").upper() == 'Y':
        print(wgu.collection_menu(word_dicts))
        book = ask_book_id(len(word_dicts))
        print(f'You are playing with words from {word_dicts[book][0]}.')
        length = ask_length(sorted(word_dicts[book][1].keys()))
        play_round(wgu.get_random_word(word_dicts[book][1], length))
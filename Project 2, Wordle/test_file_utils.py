"""Words game testing words_game_utils functions.

Author: WILLIAM JEDRZEJCZAK
Version: 11/6/2023
"""


from words_file_utils import process_word_file


def test_process_word_file():
    # Test w a correctly formatted file
    with open("test1_file.txt", "w") as file:
        file.write("WORDS Sample Collection\n")
        file.write("This is a test collection.")
    result = process_word_file("test1_file.txt")
    assert result == ("Sample Collection", "This is a test collection.")

    # Test w a file that's missing "WORDS" at the beginning
    with open("test2_file.txt", "w") as file:
        file.write("INVALID Sample Collection\n")
        file.write("This is a test collection.")
    result = process_word_file("test2_file.txt")
    assert result is None

    # Test a file missing a name for the collection
    with open("test3_file.txt", "w") as file:
        file.write("WORDS \n")
        file.write("This is a test collection.")
    result = process_word_file("test3_file.txt")
    assert result is None

    # Test an empty file
    with open("test4_file.txt", "w") as file:
        file.write("")
    result = process_word_file("test4_file.txt")
    assert result is None

    # Test for a file that does not exist
    result = process_word_file("non_existent_file.txt")
    assert result is None

    # Cleanup time wahoo
    import os
    os.remove("test1_file.txt")
    os.remove("test2_file.txt")
    os.remove("test3_file.txt")
    os.remove("test4_file.txt")

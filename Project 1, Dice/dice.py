"""Project One: Poker Dice.

Author: William Jedrzejczak

Version: 10/15 1:24 AM I DO NOT SLEEP
"""
import random
FACES = ["9", "10", "J", "Q", "K", "A"]
FACE_VALUES = {"9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}


# After I imported the faces along with their values as a dictionary
# I made roll_dice, which firstly, if the number is out of the range,
# Returns 9, otherwise, for each die (idk if that's the right word plural)
# It gets assigned a face value and added to the list of results.

# Worked on this the night of 10/13/2023


def roll_dice(numofdice, seed=0):
    """
    Roll dice return the results.

    Args:
        numofdice (int): The dice.
        seed (int): The seed.

    Returns:
        list: A list.
    """
    if numofdice < 1 or numofdice > 10:
        return ["9"]
    else:
        if seed is not None:
            random.seed(seed)
    diceresults = []
    for i in range(numofdice):
        diceresults.append(random.choice(FACES))

    return diceresults

# Definition two - Checks firstly if the number of dice is between 1 and 10
# If it is, it can return to the nedxt statement, which ensure's that the
# Values are accepted (They have to be one of the dice faces)

# Worked on morning of 10/14/2023


def are_valid(diceresults):
    """
    Check list is valid.

    Args:
        diceresults (list): A list.

    Returns:
        bool: True or False.
    """
    if diceresults is None:
        return False
    if len(diceresults) < 1 or len(diceresults) > 10:
        return False
    accepted_vals = {'9', '10', 'J', 'Q', 'K', 'A'}
    for die in diceresults:
        if die not in accepted_vals:
            return False

    return True

# This simply calculates the total value
# Of the dice as an integer value
# Given a list.

# Worked on Afternoon of 10/14/2023


def add_values(diceresults):
    """
    Calculate the total value.

    Args:
        diceresults (list): A list of dice

    Returns:
        int: The sum
    """
    if not are_valid(diceresults):
        return -1
    total_value = 0
    for eachdice in diceresults:
        if eachdice in FACE_VALUES:
            total_value += FACE_VALUES[eachdice]
    return total_value


# This provides the count of a face when given a list
# Of faces along with the individual face you're trying
# To count.

# Worked on in the evening of 10/14/2023


def num_faces(diceresults, individualface):
    """
    Count the occurrences.

    Args:
        diceresults (list): A list.
        individualface (str): The individual face.

    Returns:
        int: The count.
    """
    if not are_valid(diceresults):
        return -1
    countoftheface = 0
    for dice in diceresults:
        if dice == individualface:
            countoftheface += 1
    return countoftheface

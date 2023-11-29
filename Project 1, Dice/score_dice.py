"""Plays a text based game of Poker Dice.

Author: WILLIAM JEDRZEJCZAK
Version: 10/27/2023 CRYING THROWING UP PUKING.
"""
from dice import are_valid, add_values, num_faces, FACE_VALUES, FACES
# Constants that specify scoring types

PAIR = 1
TWO_PAIR = 2
THREE_OF_KIND = 3
FOUR_OF_KIND = 4
FIVE_OF_KIND = 5
FULL_HOUSE = 6
SMALL_STRAIGHT = 7
LARGE_STRAIGHT = 8
CHANCE = 9


def one_pair(dice_list):
    """
    Calculate the score.

    Args:
        dice_list (list): A list.

    Returns:
        int: The calculated score.
    """
    hghr_pair = 0
    for face in FACES:
        if num_faces(dice_list, face) >= 2:
            face_value = FACE_VALUES[face]
            if face_value > hghr_pair:
                hghr_pair = face_value

    if hghr_pair > 0:
        return 2 * hghr_pair
    return 0


def two_pair(dice_list):
    """
    Calculate score.

    Args:
        dice_list (list): A list.

    Returns:
        int: Score.
    """
    indivpairs = []
    count_indivpairs = 0
    for face in FACES:
        if num_faces(dice_list, face) >= 2:
            indivpairs.append(2 * FACE_VALUES[face])
            count_indivpairs += 1
        if count_indivpairs == 2:
            return int(indivpairs[0] + indivpairs[1])
    return 0


def three_of_a_kind(dice_list):
    """
    Calculate the Score.

    Args:
        dice_list (list): List.

    Returns:
        int: Score.
    """
    for face in FACES:
        if num_faces(dice_list, face) >= 3:
            return int((FACE_VALUES[face] * 3) + 10)
    return 0


def four_of_a_kind(dice_list):
    """
    Calculate the score.

    Args:
        dice_list (list): A list.

    Returns:
        int: Score.
    """
    for face in FACES:
        if num_faces(dice_list, face) >= 4:
            return int((FACE_VALUES[face] * 4) + 20)
    return 0


def five_of_kind(dice_list):
    """
    Calculate the score.

    Args:
        dice_list (list): A list.

    Returns:
        int: The calculated score.
    """
    for face in FACES:
        if num_faces(dice_list, face) == 5:
            return 100
    return 0


def full_house(dice_list):
    """
    Calculate the score.

    Args:
        dice_list (list): A list.

    Returns:
        int: Score.
    """
    three_of_a_kind = None
    pair = None
    for face in FACES:
        if num_faces(dice_list, face) == 3:
            three_of_a_kind = FACE_VALUES[face]
        if num_faces(dice_list, face) == 2:
            pair = FACE_VALUES[face]
    if three_of_a_kind is not None and pair is not None:
        return 50 + add_values(dice_list)
    return 0


def small_straight(dice_list):
    """
    Calculate the score.

    Args:
        dice_list (list): A list.

    Returns:
        int: Score.
    """
    totalscore = 0
    lastset = set()
    for i in FACES:
        if i in dice_list:
            lastset.add(i)
    if "J" in lastset:
        if "Q" in lastset:
            if "10" in lastset:
                if "9" in lastset or "K" in lastset:
                    totalscore = 70
            elif "K" in lastset:
                if "A" in lastset:
                    totalscore = 70
    else:
        totalscore = 0
    return totalscore


def large_straight(dice_list):
    """
    Calculate the score.

    Args:
        dice_list (list): A list.

    Returns:
        int: Score.
    """
    distinct_faces = set(dice_list)
    valid_faces = set(FACES)
    if valid_faces.issuperset(distinct_faces) and len(distinct_faces) == 5:
        return 95
    return 0


def chance(dice_list):
    """
    Calculate the score.

    Args:
        dice_list (list): A list.

    Returns:
        int: Score.
    """
    return add_values(dice_list)


def calculate_score(dice_list, score_type):
    """Calculate the Poker w dice_list and score_type.

    Args:
        dice_list (list): 5 values representing the outcome of the rolls.
        score_type (int): The type (category) to score.

    Returns:
        (int): The score amount.
    """
    if not are_valid(dice_list):
        return 0

    if score_type == PAIR:
        return one_pair(dice_list)

    if score_type == TWO_PAIR:
        return two_pair(dice_list)

    if score_type == THREE_OF_KIND:
        return three_of_a_kind(dice_list)

    if score_type == FOUR_OF_KIND:
        return four_of_a_kind(dice_list)

    if score_type == FIVE_OF_KIND:
        return five_of_kind(dice_list)

    if score_type == FULL_HOUSE:
        return full_house(dice_list)

    if score_type == SMALL_STRAIGHT:
        return small_straight(dice_list)

    if score_type == LARGE_STRAIGHT:
        return large_straight(dice_list)

    if score_type == CHANCE:
        return chance(dice_list)

    return 0

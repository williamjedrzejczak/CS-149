"""Project One: Poker Dice.

Author: William Jedrzejczak

Version: 10/26 6:47 LOSINGMYMINDLOSINGMYMIND.
"""
import score_dice


def test_five_of_kind():
    my_dice = ['A', 'A', 'A', 'A', 'A']
    assert score_dice.calculate_score(my_dice, 5) == 100

    my_dice = ['9', '9', '9', '9', '9']
    assert score_dice.calculate_score(my_dice, 5) == 100

    my_dice = ['9', '9', '9', '9', 'A']
    assert score_dice.calculate_score(my_dice, 5) == 0


def test_full_house():
    my_dice = ['9', '9', '9', '9', 'A']
    assert score_dice.calculate_score(my_dice, 6) == 0

    my_dice = ['9', '9', '9', 'A', 'A']
    assert score_dice.calculate_score(my_dice, 6) == 99

    my_dice = ['A', '9', '9', '9', 'A']
    assert score_dice.calculate_score(my_dice, 6) == 99


def test_one_pair():
    my_dice = ['9', '9', '10', 'J', 'K']
    assert score_dice.calculate_score(my_dice, 1) == 18


def test_one_pair_no_match():
    my_dice = ['9', '10', 'J', 'Q', 'K']
    assert score_dice.calculate_score(my_dice, 1) == 0


def test_two_pair():
    my_dice = ['9', '9', 'A', 'A', 'K']
    assert score_dice.calculate_score(my_dice, 2) == 40

    my_dice = ['K', 'K', 'J', 'J', 'A']
    assert score_dice.calculate_score(my_dice, 2) == 40

    my_dice = ['9', '9', 'A', 'J', 'K']
    assert score_dice.calculate_score(my_dice, 2) == 0

    my_dice = ['A', 'K', 'J', 'Q', '10']
    assert score_dice.calculate_score(my_dice, 2) == 0


def test_three_of_a_kind():
    my_dice = ['9', '9', '9', 'A', 'K']
    assert score_dice.calculate_score(my_dice, 3) == 37

    my_dice = ['A', 'A', 'A', 'Q', 'K']
    assert score_dice.calculate_score(my_dice, 3) == 43

    my_dice = ['9', 'A', 'J', 'Q', 'K']
    assert score_dice.calculate_score(my_dice, 3) == 0


def test_four_of_a_kind():
    my_dice = ['9', '9', '9', '9', 'A']
    assert score_dice.calculate_score(my_dice, 4) == 56

    my_dice = ['A', 'A', 'A', 'A', 'Q']
    assert score_dice.calculate_score(my_dice, 4) == 64

    my_dice = ['9', 'A', 'J', 'Q', 'K']
    assert score_dice.calculate_score(my_dice, 4) == 0


def test_small_straight():
    my_dice = ['9', '10', 'J', 'Q', 'K']
    assert score_dice.calculate_score(my_dice, 7) == 70

    my_dice = ['10', 'J', 'Q', 'K', 'A']
    assert score_dice.calculate_score(my_dice, 7) == 70

    my_dice = ['J', '10', 'Q', '9', 'K']
    assert score_dice.calculate_score(my_dice, 7) == 70

    my_dice = ['10', '10', '10', '10', '10']
    assert score_dice.calculate_score(my_dice, 7) == 0

    my_dice = ['9', '10', 'Q', 'K', 'A']
    assert score_dice.calculate_score(my_dice, 7) == 0


def test_large_straight():
    my_dice = ['9', '10', 'J', 'Q', 'K']
    assert score_dice.calculate_score(my_dice, 8) == 95

    my_dice = ['10', 'K', 'K', 'K', 'K']
    assert score_dice.calculate_score(my_dice, 8) == 0


def test_chance():
    my_dice = ['9', '10', 'J', 'Q', 'K']
    assert score_dice.calculate_score(my_dice, 9) == 49

    my_dice = ['A', 'A', 'A', 'A', 'A']
    assert score_dice.calculate_score(my_dice, 9) == 55

    my_dice = ['9', '9', '9', '9', '9']
    assert score_dice.calculate_score(my_dice, 9) == 45

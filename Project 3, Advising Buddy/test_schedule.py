"""Unit tests for schedule_utils.

Author: William Jedrzejczak
Version: 11/27/2023 11:40 Right before Class.
"""

from schedule_utils import schedule_to_json, json_to_schedule, save_schedule, load_schedule, get_duplicates
import schedule_utils


def test_schedule_to_json(): # This Passed DONT TOUCH
    # Test 1
    schedule = []
    result = schedule_to_json(schedule)
    assert result == []

    # Test w Schedule
    schedule = [{'CS 149'}, {'CS 227', 'CS 159'}, {'ALGEBRA'}]
    result = schedule_to_json(schedule)
    expected_result = [
        ["ALGEBRA"],
        ["CS 149"],
        sorted(["CS 159", "CS 227"])
    ]
    assert sorted(result) == sorted(expected_result)


def test_json_to_schedule(): # This Passed DONT TOUCH
    # Test w empty JSON
    json_schedule = []
    result = json_to_schedule(json_schedule)
    assert result == []

    # Test w non-empty JSON
    json_schedule = [['ALGEBRA'], ['CS 149'], ['CS 159', 'CS 227']]
    result = json_to_schedule(json_schedule)
    expected_result = [{'ALGEBRA'}, {'CS 149'}, {'CS 159', 'CS 227'}]
    assert result == expected_result

def test_save_load_schedule(): # Passed DONT TOUCH
    # Test w First Case
    schedule = [{'CS 149'}, {'CS 227', 'CS 159'}, {'ALGEBRA'}]

    # Save
    save_schedule(schedule, "test_schedule.json")

    # Load
    loaded_schedule = load_schedule("test_schedule.json")

    # Assert
    assert loaded_schedule == schedule

    # Test w Second Case
    # Different Schedule
    another_schedule = [{'MATH 101'}, {'PHYS 201'}, {'CHEM 301'}]

    # Save
    save_schedule(another_schedule, "test_schedule_another.json")

    # Load
    loaded_another_schedule = load_schedule("test_schedule_another.json")

    # Assert
    assert loaded_another_schedule == another_schedule


def test_get_duplicates(): # Passed DONT TOUCH
    # Test w No Dupes
    schedule = [{'CS 149'}, {'CS 227', 'CS 159'}]
    result = get_duplicates(schedule)
    assert result == set()

    # Test w Dupes
    schedule = [{'CS 149'}, {'CS 227', 'CS 149'}]
    result = get_duplicates(schedule)
    assert result == {'CS 149'}
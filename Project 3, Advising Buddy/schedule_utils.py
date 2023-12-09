"""Utility functions for working with course schedules.

A course schedule is a list of sets where each entry in the list
represents an academic term, and the entries in the sets are strings
representing the course ids of courses taken during that term.

Author: William Jedrzejczak
Version: 11/29/2023
"""

import json


def schedule_to_json(schedule):
    """Convert a course schedule to a format suitable for saving as JSON.

    The provided schedule will not be modified.

    Args:
        schedule (list): A list of sets.

    Returns:
        list: A list of lists.
    """
    return [sorted(list(term)) for term in schedule]


def json_to_schedule(schedule_list):
    """Convert a list of lists to a list of sets.

    The elements in each list will be stored in alphabetical order.
    The provided list will not be modified.

    Args:
        schedule_list (list): A list of lists.

    Returns:
        list: A list of sets.

    """
    return [set(sorted(term)) for term in schedule_list]


def save_schedule(schedule, filename):
    """Save a course schedule to a JSON file.

    The course schedule is represented as a list of sets, where each
    set contains the course ids (strings) for the corresponding
    semester.

    Within each semester, the course ids will be stored in alphabetical
    order in the resulting JSON file.

    Args:
        schedule (list): The course schedule.
        filename (str): The filename for the JSON file.

    """
    json_schedule = [sorted(list(term)) for term in schedule]

    # Save the JSON data to the file
    with open(filename, 'w') as file:
        json.dump(json_schedule, file, indent=4)


def load_schedule(filename):
    """Load a course schedule from an JSON file.

    The return value will be a list of sets, where each set contains
    the course ids (strings) for the corresponding semester.

    Args:
        filename (str): The filename of the JSON file.

    Returns:
        list: A list of sets representing the course schedule.

    """
    with open(filename, 'r') as file:
        json_schedule = json.load(file)

    # Convert JSON data to the internal format
    return [set(term) for term in json_schedule]


def get_duplicates(schedule):
    """Get duplicate courses in a schedule.

    The resulting set will be empty if there are no duplicates.

    Args:
        schedule (list): The course schedule.

    Returns:
        set: A set of duplicate courses.
    """
    observed_courses = set()
    duplicate_courses = set()

    for term in schedule:
        for course in term:
            if course in observed_courses:
                duplicate_courses.add(course)
            else:
                observed_courses.add(course)

    return duplicate_courses

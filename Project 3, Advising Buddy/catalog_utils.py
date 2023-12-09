"""Utility functions for working with catalog information.

Author: Will Jedrzejczak
Version: 11/29/2023
"""

import json
import textwrap


def parse_credits(credits):
    """Return a tuple of ints representing the possible credit values.

    Examples:
    >>> parse_credits("3")
    (3,)
    >>> parse_credits("1-4")
    (1, 2, 3, 4)

    Args:
        credits (str): The credits string.

    Returns:
        tuple: An ordered tuple of all possible credit values.
    """
    if '-' in credits:
        start, end = credits.split('-')
        return tuple(range(int(start), int(end) + 1))
    else:
        return (int(credits),)


def json_to_catalog(json_dict):
    """Convert from the json catalog format to the correct internal format.

    This will return an exact copy of the provided dictionary except for the
    following:

    * The lists of prerequisite course ids will be converted to sets.
    * The credit strings will be converted to integer tuples (using
    the parse_credits function)

    Args:
        json_dict (dict): A catalog dictionary as ready by the json module.

    Returns:
        dict: A catalog dictionary in the correct internal format.

    """
    catalog = {}

    for course_id, course_info in json_dict.items():
        internal_info = {
            'name': course_info['name'],
            'description': course_info['description'],
            'credits': parse_credits(course_info['credits']),
            'prerequisites': set(course_info['prerequisites'])
        }
        catalog[course_id] = internal_info

    return catalog


def load_catalog(filename):
    """Read course information from an JSON file and return a dictionary.

    Args:
        filename (str): The filename of the JSON file.

    Returns:
        dict: A dictionary containing course information.
    """
    with open(filename, 'r') as file:
        json_data = json.load(file)

    catalog = {}

    for course_id, course_info in json_data.items():
        internal_info = {
            'name': course_info['name'],
            'description': course_info['description'],
            'credits': parse_credits(course_info['credits']),
            'prerequisites': set(course_info['prerequisites'])
        }
        catalog[course_id] = internal_info

    return catalog


def get_dependencies(course_id, catalog):
    """Get the all dependencies for a course.

    This function will return the prerequisites for the course, plus
    all prerequisites for those prerequisites, and so on.

    Args:
        course_id (str): The ID of the course.
        catalog (dict): The dictionary containing course information.

    Returns:
        set: A set of course dependencies.

    """
    def find_dependencies(course_id, dependencies):
        course_info = catalog.get(course_id)

        if course_info:
            prerequisites = course_info['prerequisites']
            dependencies.update(prerequisites)
            for prerequisite in prerequisites:
                find_dependencies(prerequisite, dependencies)

    dependencies = set()
    find_dependencies(course_id, dependencies)
    return dependencies


def format_course_info(course_id, catalog, width=40):
    """Format course information for display.

    The resulting string will have five fields: Name, Description,
    Credits, Prerequisites, and Dependencies. Each field will be
    separated by a blank line and each will be wrapped to the maximum
    allowable number of characters. The string will not end in a newline.

    Args:
        course_id (str): The ID of the course.
        catalog (dict): The dictionary containing course information.
        width (int, optional): The width for text wrapping. Defaults to 40.

    Returns:
        str: Formatted course information.
    """
    course_info = catalog.get(course_id, {})
    name = f'Name: {course_info.get("name", "N/A")}'
    description = f'Description: {course_info.get("description", "N/A")}'
    credits = f'Credits: {"-".join(map(str, course_info.get("credits", ())))}'

    prereq = course_info.get('prerequisites', set())
    if prereq:
        prereq = ', '.join(sorted(prereq))
    else:
        prereq = ''
    prereq = f'Prerequisites: {prereq}'

    deps = get_dependencies(course_id, catalog)
    if deps:
        deps = ', '.join(sorted(deps))
    else:
        deps = ''
    deps = f'Dependencies: {deps}'

    formatted_info = '\n\n'.join([
        textwrap.fill(name, width),
        textwrap.fill(description, width),
        textwrap.fill(credits, width),
        textwrap.fill(prereq, width),
        textwrap.fill(deps, width)
    ])

    return formatted_info


def total_credits(schedule, catalog):
    """Calculate the range of total credits in a schedule.

    Args:
        schedule (list): The course schedule.
        catalog (dict): The dictionary containing course information.

    Returns:
        tuple: A two entry tuple where the first entry is the minimum
            total credits for the schedule and the second is the maximum total
            credits.
    """
    min_credits = 0
    max_credits = 0

    for semester in schedule:
        for course_id in semester:
            course_info = catalog.get(course_id)
            if course_info:
                credits = course_info.get('credits')
                if credits:
                    if isinstance(credits, tuple):
                        min_credits += min(credits)
                        max_credits += max(credits)
                    else:
                        min_credits += credits
                        max_credits += credits

    return min_credits, max_credits


def available_classes(schedule, semester, catalog):
    """Get the available classes for a semester based on the current schedule.

    A course is available for the indicated semester if it is not
    already present somewhere in the schedule, and all of the
    prerequisites have been fulfilled in some previous semester.

    Args:
        schedule (list): The current course schedule.
        semester (int): The semester for which to find available classes.
        catalog (dict): The dictionary containing course information.

    Returns:
        set: A set of available classes for the specified semester.

    """
    all_courses_in_schedule = \
        set(course for semr_courses in schedule for course in semr_courses)
    completed_prerequisites = set()
    for i in range(semester):
        completed_prerequisites.update(course for course in schedule[i])
    available_courses = set()
    for course, info in catalog.items():
        if course not in all_courses_in_schedule:
            if set(info["prerequisites"]) - completed_prerequisites == set():
                available_courses.add(course)

    return available_courses


def check_prerequisites(schedule, catalog):
    """Check for courses in a schedule with unmet prerequisites.

    Args:
        schedule (list): The course schedule.
        catalog (dict): The dictionary containing course information.

    Returns:
        set: A set of courses with unmet prerequisites.
    """
    classsched = set()
    preqnotmet = set()
    noset = set()

    for course_set in schedule:
        if len(course_set) > 1:
            for course in course_set:
                for preq in catalog[course]["prerequisites"]:
                    if any(
                        dependency in course_set
                        for dependency in catalog[course]["prerequisites"]
                    ):
                        preqnotmet.add(course)
        for course in course_set:
            classsched.add(course)
    for course in classsched:
        for preq in catalog[course]["prerequisites"]:
            if preq == noset:
                continue
            if preq not in classsched:
                preqnotmet.add(course)
    return preqnotmet

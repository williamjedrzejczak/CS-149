"""Unit tests for catalog_utils.

Author: William Jedrzejczak
Version: 11/27/2023 in the depths of the night.
"""
import json
import textwrap
from catalog_utils import parse_credits, json_to_catalog, load_catalog, get_dependencies, format_course_info, \
    total_credits, available_classes, check_prerequisites
import catalog_utils

def test_parse_credits(): # Completed Done
    # Test w Single Cred
    result = parse_credits("3")
    assert result == (3,)

    # Test w Range
    result = parse_credits("1-4")
    assert result == (1, 2, 3, 4)


def test_json_to_catalog(): # Completed Done
    # Test w empty
    json_dict = {}
    result = json_to_catalog(json_dict)
    assert result == {}

    # Test w non-empty
    json_dict = {
        'CS 101': {'name': 'Introduction to CS', 'credits': '3', 'description': 'An introductory course.', 'prerequisites': []},
        'CS 102': {'name': 'Advanced CS', 'credits': '4-5', 'description': 'A more advanced course.', 'prerequisites': ['CS 101']}
    }
    result = json_to_catalog(json_dict)
    expected_result = {
        'CS 101': {'name': 'Introduction to CS', 'credits': (3,), 'description': 'An introductory course.', 'prerequisites': set()},
        'CS 102': {'name': 'Advanced CS', 'credits': (4, 5), 'description': 'A more advanced course.', 'prerequisites': {'CS 101'}}
    }
    assert result == expected_result


def test_load_catalog():
    result = load_catalog("japn_catalog.json")
    assert isinstance(result, dict)
    for course_id, course_info in result.items():
        assert isinstance(course_info, dict)
        assert 'credits' in course_info
        assert 'description' in course_info
        assert 'name' in course_info
        assert 'prerequisites' in course_info
        assert isinstance(course_info['credits'], tuple)
        assert isinstance(course_info['prerequisites'], (list, set))

    # Check spec courses
    assert 'JAPN 101' in result
    assert 'JAPN 102' in result
    assert 'JAPN 231' in result


def test_get_dependencies(): # Done
    # Test w no Dep
    catalog = {
        'CS 101': {'name': 'Introduction to CS', 'prerequisites': set()},
        'CS 102': {'name': 'Advanced CS', 'prerequisites': {'CS 101'}}
    }
    result = get_dependencies('CS 101', catalog)
    assert result == set()

    # Test w Dep
    result = get_dependencies('CS 102', catalog)
    assert result == {'CS 101'}


def test_total_credits():
    # Test Calc
    schedule = [{'JAPN 101'}, {'JAPN 102'}, {'JAPN 231'}]
    catalog = {
        'JAPN 101': {'name': 'Elementary Japanese I', 'credits': (4,), 'description': 'The fundamentals of Japanese through listening, speaking, reading, and writing.', 'prerequisites': []},
        'JAPN 102': {'name': 'Elementary Japanese II', 'credits': (4,), 'description': 'The fundamentals of Japanese through listening, speaking, reading, and writing. Practice in pronunciation and development of comprehension.', 'prerequisites': ['JAPN 101']},
        'JAPN 231': {'name': 'Intermediate Japanese I', 'credits': (3, 4), 'description': 'A thorough review of grammar, vocabulary building, conversation, composition, and reading.', 'prerequisites': ['JAPN 102']}
    }

    # Test w Credits
    result = total_credits(schedule, catalog)
    assert result == (11, 12)

    # Test w Diff Schedule
    another_schedule = [{'JAPN 101'}, {'JAPN 102'}]
    another_result = total_credits(another_schedule, catalog)
    assert another_result == (8, 8)


def test_available_classes():
    catalog = {
        "JAPN 101": {"prerequisites": set()},
        "JAPN 102": {"prerequisites": {"JAPN 101"}},
        "JAPN 231": {"prerequisites": {"JAPN 102"}},
    }

    # Define semester variable
    semester = 1

    # Test case 1
    schedule_1 = [{'JAPN 101'}, set(), set()]
    available_classes_1 = available_classes(schedule_1, semester, catalog)
    assert available_classes_1 == {'JAPN 102'}

    # Test case 2
    schedule_2 = [{'JAPN 101'}, set(), set()]
    available_classes_2 = available_classes(schedule_2, 0, catalog)
    assert available_classes_2 == set()


def test_check_prerequisites():
    catalog = {
        "JAPN 101": {"prerequisites": set()},
        "JAPN 102": {"prerequisites": {"JAPN 101"}},
        "JAPN 231": {"prerequisites": {"JAPN 102"}},
    }

    # Test case 1
    schedule_1 = [{'JAPN 101'}, set(), {'JAPN 231'}]
    unmet_prerequisites_1 = check_prerequisites(schedule_1, catalog)
    assert unmet_prerequisites_1 == {'JAPN 231'}

    # Test case 2
    schedule_2 = [set(), {'JAPN 102'}, {'JAPN 231'}]
    unmet_prerequisites_2 = check_prerequisites(schedule_2, catalog)
    assert unmet_prerequisites_2 == {'JAPN 102'}


# We're providing tests for format_course_info() because these
# kinds of tests are particularly annoying to write.

def test_format_course_info(): # Done
    catalog = catalog_utils.load_catalog("japn_catalog.json")

    # Test the default width...
    actual = catalog_utils.format_course_info("JAPN 231", catalog)
    expect = """Name: Intermediate Japanese I

Description: A thorough review of
grammar, vocabulary building,
conversation, composition, and reading.

Credits: 3-4

Prerequisites: JAPN 102

Dependencies: JAPN 101, JAPN 102"""
    assert actual == expect

    #  Test an alternate width...
    actual = catalog_utils.format_course_info("JAPN 231", catalog, width=80)
    expect = """Name: Intermediate Japanese I

Description: A thorough review of grammar, vocabulary building, conversation,
composition, and reading.

Credits: 3-4

Prerequisites: JAPN 102

Dependencies: JAPN 101, JAPN 102"""
    assert actual == expect

    #  Test a different course and a different width...
    actual = catalog_utils.format_course_info("JAPN 101", catalog, width=50)
    expect = """Name: Elementary Japanese I

Description: The fundamentals of Japanese through
listening, speaking, reading, and writing.

Credits: 4

Prerequisites:

Dependencies:"""
    assert actual == expect
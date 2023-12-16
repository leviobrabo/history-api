from pytest import mark, raises
from history_api.presidents_location import get_president_by_location, LANGUAGES
from pathlib import Path
import json
import os


def test_should_work_with_capitalized_lang():
    lang = 'EN'
    location = 'United States'
    result = get_president_by_location(lang, location)
    assert result


def test_should_work_with_capitalized_location():
    lang = 'EN'
    location = 'ISRAEL'
    result = get_president_by_location(lang, location)
    assert result


def test_should_return_an_error_saying_that_the_lang_does_not_exist():
    lang = 'KS'
    location = 'South Africa'
    expected_error_message = f"This language does not exist, available languages are: {list(LANGUAGES.keys())}"

    with raises(FileNotFoundError) as error:
        get_president_by_location(lang, location)

    assert expected_error_message in str(error.value)


def test_should_return_an_error_for_invalid_location():
    lang = 'DE'
    non_listed_country = 'Nepal'

    expected_error_message = f"Country '{non_listed_country}' is not available in the location list."

    try:
        get_president_by_location(lang, non_listed_country)
        assert False, f"Expected ValueError with message '{expected_error_message}' was not raised"
    except ValueError as e:
        assert str(e) == expected_error_message


@mark.parametrize("lang", LANGUAGES.keys())
def test_all_locations_for_language(lang):
    locations = [
        'United States', 'China', 'Japan', 'Germany', 'India', 'United Kingdom',
        'France', 'Brazil', 'Italy', 'Canada', 'South Korea', 'Russia', 'Australia',
        'Spain', 'Mexico', 'Indonesia', 'Turkey', 'Argentina', 'Israel', 'South Africa'
    ]

    for location in locations:
        result = get_president_by_location(lang, location)
        assert result is not None, f"Failed for lang: {lang}, location: {location}"

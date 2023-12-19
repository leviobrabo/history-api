from pytest import mark, raises
from history_api.curiosity_month_day import search_curiosity_month_day, LANGUAGES
from pathlib import Path
import json
import os


def test_should_work_with_capitalized_lang_month():
    lang = 'EN'
    month = '3'
    day = '6'
    result = search_curiosity_month_day(lang, month, day)
    assert result


def test_should_return_an_error_saying_that_the_lang_and_month_does_not_exist():
    lang = 'KS'
    month = '12'
    day = '2'
    expected_error_message = f"This language does not exist, available languages are: {list(LANGUAGES.keys())}"

    with raises(ValueError) as error:
        search_curiosity_month_day(lang, month, day)

    assert expected_error_message in str(error.value)


def test_should_return_an_error_when_the_event_month_is_non_existent():
    lang = 'ru'
    month = '0'
    day = '2'
    expected_error_message = "Invalid month number. Please choose a month between 1 and 12."

    with raises(ValueError) as error:
        search_curiosity_month_day(lang, month, day)

    assert expected_error_message in str(error.value)


def test_should_return_an_error_when_the_event_day_is_invalid():
    lang = 'en'
    month = '2'
    day = '30'

    expected_error_message = "Please set the correct day for the month"

    with raises(AssertionError) as error:
        try:
            search_curiosity_month_day(lang, month, day)
        except AssertionError as e:
            assert expected_error_message in str(e)
        else:
            assert False, "Expected a AssertionError to be raised, but no error was raised."

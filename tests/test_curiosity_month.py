from pytest import mark, raises
from history_api.curiosity_month import search_curiosity_month, LANGUAGES
from pathlib import Path
import json
import os


def test_should_work_with_capitalized_lang_month():
    lang = 'EN'
    month = '3'
    result = search_curiosity_month(lang, month)
    assert result


def test_should_return_an_error_saying_that_the_lang_and_month_does_not_exist():
    lang = 'KS'
    month = '12'
    expected_error_message = f"This language does not exist, available languages are: {list(LANGUAGES.keys())}"

    with raises(ValueError) as error:
        search_curiosity_month(lang, month)

    assert expected_error_message in str(error.value)


def test_should_return_an_error_when_the_event_month_is_non_existent():
    lang = 'ru'
    month = '0'
    expected_error_message = "Invalid month number. Please choose a month between 1 and 12."

    with raises(ValueError) as error:
        search_curiosity_month(lang, month)

    assert expected_error_message in str(error.value)


def test_json_files_have_expected_keys():
    data_dir = Path(__file__).resolve().parent / '..' / \
        'history_api' / 'data' / 'curiosity'
    missing_files = []

    for lang in LANGUAGES.keys():
        for month in range(1, 13):
            json_file = data_dir / f"curiosity-{lang}.json"

            if not json_file.exists():
                missing_files.append(
                    f"JSON file {json_file} for language {lang} and month {month}")

    assert not missing_files, f"Missing files: {', '.join(missing_files)}"

from pytest import mark, raises
from history_api.events import search_all_events, LANGUAGES
from pathlib import Path
import json
import os


def test_should_work_with_capitalized_lang():
    lang = 'EN'
    result = search_all_events(lang)
    assert result


def test_should_return_an_error_saying_that_the_lang_does_not_exist():
    lang = 'KS'

    expected_error_message = f"This language does not exist, available languages are: {list(LANGUAGES.keys())}"

    with raises(FileNotFoundError) as error:
        search_all_events(lang)

    assert expected_error_message in str(error.value)


def test_json_files_have_expected_keys():
    expected_keys = [
        f"{month}-{day}" for month in range(1, 13) for day in range(1, 32)]

    data_dir = Path(__file__).resolve().parent / '..' / \
        'history_api' / 'data' / 'events'

    missing_files = []

    for lang in LANGUAGES.keys():
        json_file = data_dir / f"events-{lang}.json"

        if not os.path.exists(json_file):
            missing_files.append(f"JSON file {json_file} for language {lang}")

    assert not missing_files, f"Missing files: {', '.join(missing_files)}"

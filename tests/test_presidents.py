from pytest import mark, raises
from history_api.presidents import search_all_presidents, LANGUAGES
from pathlib import Path
import json
import os


def test_should_work_with_capitalized_lang():
    lang = 'EN'
    result = search_all_presidents(lang)
    assert result


def test_should_return_an_error_saying_that_the_lang_does_not_exist():
    lang = 'KS'

    expected_error_message = f"This language does not exist, available languages are: {list(LANGUAGES.keys())}"

    with raises(FileNotFoundError) as error:
        search_all_presidents(lang)

    assert expected_error_message in str(error.value)


def test_json_files_have_expected_keys():
    expected_keys = [str(key) for key in range(1, 653)]

    data_dir = Path(__file__).resolve().parent / '..' / \
        'history_api' / 'data' / 'presidents'

    missing_keys = []

    for lang in LANGUAGES.keys():
        json_file = data_dir / f"presidents-{lang}.json"

        if os.path.exists(json_file):
            with open(json_file, 'r', encoding='utf-8') as file:
                json_data = json.load(file)
                missing_lang_keys = [
                    key for key in expected_keys if key not in json_data]

                if missing_lang_keys:
                    missing_keys.append(
                        f"Language: {lang}, Missing keys: {', '.join(missing_lang_keys)}")
        else:
            missing_keys.append(
                f"JSON file {json_file} for language {lang} is missing")

    assert not missing_keys, f"Missing keys: {', '.join(missing_keys)}"

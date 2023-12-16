import random
import pytest
from pytest import mark, raises
from history_api.presidents_range_id import get_presidents_range, LANGUAGES
from pathlib import Path
import json
import os


def test_should_work_with_capitalized_lang():
    lang = 'EN'
    start_id = '1'
    end_id = '10'

    result = get_presidents_range(lang, start_id, end_id)
    assert result


def test_should_return_an_error_saying_that_the_lang_does_not_exist():
    lang = 'KS'
    start_id = '6'
    end_id = '10'

    expected_error_message = f"Unsupported language: {lang.lower()}"

    with raises(KeyError) as error:
        get_presidents_range(lang, start_id, end_id)

    assert expected_error_message.lower() in str(error.value).lower()


def test_get_president_id_less_than_1():
    lang = 'en'
    invalid_id = '0'
    end_id = '4'
    with pytest.raises(KeyError) as error:
        get_presidents_range(lang, invalid_id, end_id)
    assert 'Provided president IDs are out of range' in str(error.value)


def test_get_president_id_greater_than_652():
    lang = 'en'
    start_id = '650'
    invalid_id = '653'
    with pytest.raises(KeyError) as error:
        get_presidents_range(lang, start_id, invalid_id)
    assert 'Provided president IDs are out of range' in str(error.value)


def test_get_president_id_random_ranges(lang, start_id, end_id):
    with pytest.raises(KeyError):
        get_presidents_range(lang, start_id, end_id)


def test_end_id_greater_than_start_id():
    lang = 'en'
    start_id = '5'
    end_id = '10'

    result = get_presidents_range(lang, start_id, end_id)

    assert int(end_id) > int(
        start_id), "end_id should be greater than start_id"


def generate_random_ids():
    start_id = random.randint(1, 651)
    end_id = random.randint(start_id + 1, 652)
    return str(start_id), str(end_id)


@pytest.mark.parametrize("lang, start_id, end_id", [
    (random.choice(list(LANGUAGES.keys())), *generate_random_ids()) for _ in range(2)
])
def test_get_president_id_random_ranges(lang, start_id, end_id):
    get_presidents_range(lang, start_id, end_id)

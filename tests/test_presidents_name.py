from pytest import mark, raises
from history_api.presidents_name import get_president_by_name, LANGUAGES


def test_should_work_with_capitalized_lang():
    lang = 'EN'
    name = 'Donald Trump'
    result = get_president_by_name(lang, name)
    assert result


def test_should_work_with_capitalized_name():
    lang = 'EN'
    name = 'Jair'
    result = get_president_by_name(lang, name)
    assert result


def test_should_return_an_error_saying_that_the_lang_does_not_exist():
    lang = 'KS'
    name = 'Vladimir Putin'
    expected_error_message = f"This language does not exist, available languages are: {list(LANGUAGES.keys())}"

    with raises(FileNotFoundError) as error:
        get_president_by_name(lang, name)

    assert expected_error_message in str(error.value)


def test_should_return_an_error_for_invalid_president():
    lang = 'EN'
    name = 'Calor Pinto'

    expected_error_message = f"President '{name}' is not available in the list."

    with raises(ValueError) as error:
        get_president_by_name(lang, name)

    assert expected_error_message in str(error.value)

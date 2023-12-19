import json
from pathlib import Path
import calendar

from history_api.plugins.languages import LANGUAGES


def get_curiosity_path():
    return Path(__file__).resolve().parent / 'data' / 'curiosity'


def search_curiosity_month_day(lang: str, month: str, day: str) -> dict[str, list[str]]:
    """
    Searches for a specific curiosity by date and language.

    Args:
        lang (str): The language of the curiosity (e.g., 'pt' for Portuguese).
        month (str): The desired month number in the 'MM' format.
        day (str): The desired day number in the 'DD' format.

    Returns:
        list: List of curiosity for the provided date in HTML format, if found, otherwise returns an empty list.

    Raises:
        ValueError: If the lang is not valid or if the month is not a number between 1 and 12.
        AssertionError: The day is not in the month parameter

    Examples:
        >>> search_curiosity_month('uk', '9', '25') # doctest: +SKIP
            {
                  "9-25": {
                        "curiosity": [
                            {
                                "text": "25 вересня 1513 року іспанський дослідник Васко Нуньєс де Бальбоа став першим європейцем, який побачив Тихий океан після перетину Панамського перешийка."
                            },
                            {
                                "text1": "25 вересня 1957 року дев’ятеро чорношкірих учнів вступили до центральної середньої школи Літтл-Рок у Літл-Рок, штат Арканзас, під федеральним захистом, що стало важливою віхою в русі за громадянські права в Сполучених Штатах."
                            }
                        ]
            }
    """
    lang = lang.lower()
    if lang not in LANGUAGES:
        raise ValueError(
            f"This language does not exist, available languages are: {list(LANGUAGES.keys())}")

    month = int(month)
    if month < 1 or month > 12:
        raise ValueError(
            "Invalid month number. Please choose a month between 1 and 12.")

    days_in_month = {
        1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    day = int(day)
    if day < 1 or day > days_in_month.get(month):
        month_name = calendar.month_name[month]
        raise AssertionError(
            f"Invalid day number for {month_name}. Please choose a day between 1 and {days_in_month.get(month)}.")

    json_dir = get_curiosity_path()
    json_file = json_dir / f"curiosity-{lang}.json"
    curiosity_date = f"{month}-{day}"
    curiosity_for_date = []

    if json_file.exists():
        with open(json_file, 'r', encoding='utf-8') as file:
            curiosity = json.load(file)
            if curiosity_date in curiosity:
                curiosity_for_date = curiosity[curiosity_date]

    return curiosity_for_date

    
    
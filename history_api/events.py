import json
from pathlib import Path

from history_api.plugins.languages import LANGUAGES


def get_events_path():
    return Path(__file__).resolve().parent / 'data' / 'events'


def search_all_events(lang: str) -> dict[str, list[str]]:
    """
    Searches for all events from a JSON file by language.

    Args:
        lang: The language of the events (e.g., 'pt' for Portuguese).

    Returns:
         Dictionary containing all events for the provided language.

    Raises:
        FileNotFoundError: If the lang is not valid.

    Examples:
        >>> search_all_events('en') # doctest: +SKIP
        {
            "1-1": [
                "[1/1/1502] • Portuguese navigators arrived at the coast of the South American continent and named the current city Rio de Janeiro.",
                "[1/1/1764] • In France, Wolfgang Amadeus Mozart, at the age of 8, plays the piano for the Royal Family in Versailles.",
                "[1/1/1776] • The leader of the American Revolution, George Washington presents the first national flag of the United States.",
                "[1/1/1797] • Albany replaces New York City as capital of the state of New York.",
                # More events...
            ],
            # More date-event pairs...
        }

        >>> search_all_events('RU') # doctest: +SKIP
        {
            "1-1": [
                "[1/1/1502] • Португальские мореплаватели прибыли к побережью южноамериканского континента и назвали нынешний город Рио-де-Жанейро.",
                "[1/1/1764] • Во Франции Вольфганг Амадей Моцарт в возрасте 8 лет играет на фортепиано в королевской семье в Версале.",
                "[1/1/1776] • Лидер Североамериканской революции Джордж Вашингтон представляет первый национальный флаг Соединенных Штатов.",
                "[1/1/1797] • Олбани заменяет Нью-Йорк в качестве столицы штата Нью-Йорк.",
                # More events...
            ],
            # More date-event pairs...
        }
    """
    lang = lang.lower()
    if lang not in LANGUAGES:
        raise FileNotFoundError(
            f"This language does not exist, available languages are: {list(LANGUAGES.keys())}")

    json_dir = get_events_path()
    json_file = json_dir / f"events-{lang}.json"

    with open(json_file, 'r', encoding='utf-8') as file:
        return json.load(file)

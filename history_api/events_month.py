import json
from pathlib import Path

from history_api.plugins.languages import LANGUAGES


def get_events_path():
    return Path(__file__).resolve().parent / 'data' / 'events'


def search_events_month(lang: str, month: str) -> dict[str, list[str]]:
    """
    Searches for all events in a month from a JSON file by language.

    Args:
        lang (str): The language of the events (e.g., 'pt' for Portuguese).
        month (str): The desired month number in the 'M' format.

    Returns:
        dict: Dictionary containing events for the provided month in the 'M-D' format
              and the value is a list of events for that date.

    Raises:
        ValueError: If the lang is not valid or if the month is not a number between 1 and 12.

    Examples:
        >>> search_events_month('en', '5') # doctest: +SKIP
        {
            "5-1": [
                "[1/5/1842] • The Brazilian Federal Chamber is dissolved by decree for the first time.",
                "[1/5/1844] • Samuel Morse sends the first telegraph message.",
                "[1/5/1886] • North American workers at an industry in Chicago go on strike demanding an eight-hour workday. Police repression of the movement caused the death of a worker. For To protest this tragedy, a demonstration is organized in which seven police officers are killed. Eight leaders of the protesters are tried for murder and four of them are sentenced to death.",
                "[1/5/1889] • Socialists meeting in Paris resolve that from the year 1890, May 1st would be celebrated as International Workers' Day in memory of the Chicago victims.",
                # More events...
            ],
            # More date-event pairs...
            "5-31": [
                "[5/31/1790] • The Copyright Act is signed by President George Washington, protecting copyrights in books, maps, and other written materials.",
                "[5/31/1907] • Taxis arrive in New York City from Paris. These new taxis are the first in the United States.",
                "[5/31/1910] • The South Africa Act unifies and guarantees self-government to the British colonies in the region. The new constitution concentrates power in the hands of the entire white parliament, and denies participation of black representatives.",
                "[5/31/1911] • In Belfast, the White Star Titanic is presented as one of the largest floating vessels. The ship sinks on its maiden voyage in April 1912.",
                "[5/31/1945] • In China, General Chiang Kai-Shek resigns as prime minister, but continues as president of the country. His successor is Dr. TV Soong.",
                # More events...
            ],
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

    json_dir = get_events_path()
    json_file = json_dir / f"events-{lang}.json"
    events_month = {}

    with open(json_file, 'r', encoding='utf-8') as file:
        events = json.load(file)

        for key, value in events.items():
            if key.startswith(f"{month}-"):
                events_month[key] = value

        return events_month

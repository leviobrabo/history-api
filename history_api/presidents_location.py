import json
from pathlib import Path

from history_api.plugins.languages import LANGUAGES


def get_presidents_path():
    return Path(__file__).resolve().parent / 'data' / 'presidents'


def get_president_by_location(lang, location):
    """
    Retrieves a president by location from a JSON file by language.

    Location always written in English...

    Location: United States, China, Japan, Germany, India, United Kingdom, France, Brazil, Italy, Canada, South Korea, Russia, Australia, Spain, Mexico, Indonesia, Turkey, Argentina, and South Africa.

    Args:
        lang (str): The language code (e.g., 'pt' for Portuguese).
        location (str): The location of the president. (in English)

    Returns:
        dict: Details of the president with the given location.

    Raises:
        FileNotFoundError: If the JSON file corresponding to the language is not found.
        ValueError: If the provided location does not exist.

    Examples:
        >>> search_all_presidents('en', 'Japan') # doctest: +SKIP
        {
        "93": {
            "title": "Prime Minister of Japan 🇯🇵",
            position: "1",
            "name": "Ito Hirobumi",
            "photo": "https://pt.wikipedia.org/wiki/Ficheiro:IT%C5%8C_Hirobumi.jpg",
            "broken": "none",
            "year_of_office": "1885-1888",
            "vice-presidente": "Não informado",
            "local": "Japan"
            },
        "94": {
            "title": "Prime Minister of Japan 🇯🇵",
            position: "2",
            "name": "Kuroda Kiyotaka",
            "photo": "https://pt.wikipedia.org/wiki/Ficheiro:Kiyotaka_Kuroda_formal_cropped.jpg",
            "broken": "none",
            "year_of_office": "1888-1889",
            "vice-presidente": "Não informado",
            "local": "Japan"
            },
            # More presidents...
        "156": {
            "title": "Prime Minister of Japan 🇯🇵",
            "position": "64",
            "name": "Fumio Kishida",
            "photo": "https://pt.wikipedia.org/wiki/Ficheiro:Fumio_Kishida_20211005.jpg",
            "broken": "Liberal Democrat",
            "year_of_office": "2021-fiscal year",
            "vice-presidente": "Não informado",
            "local": "Japan"
            }
        }
    """
    lang = lang.lower()

    if lang not in LANGUAGES:
        raise FileNotFoundError(
            f"This language does not exist, available languages are: {list(LANGUAGES.keys())}")

    presidents_path = get_presidents_path()
    json_file = presidents_path / f"presidents-{lang}.json"

    location_lower = location.lower()
    stored_location_lower = None

    with open(json_file, 'r', encoding='utf-8') as file:
        presidents_data = json.load(file)

        for details in presidents_data.values():
            stored_location_lower = details.get('local').lower()

            if (
                stored_location_lower == location_lower
                or stored_location_lower == location_lower.title()
                or stored_location_lower == location_lower.upper()
                or stored_location_lower == location_lower.capitalize()
            ):
                return details

    raise ValueError(
        f"Country '{location}' is not available in the location list.")

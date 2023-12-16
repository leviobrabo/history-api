import json
from pathlib import Path

from history_api.plugins.languages import LANGUAGES


def get_presidents_path():
    return Path(__file__).resolve().parent / 'data' / 'presidents'


def get_president_by_id(lang: str, id: str) -> dict[str, dict[str, str]]:
    """
    Retrieves a president by ID from a JSON file by language.

    Args:
        lang (str): The language code (e.g., 'pt' for Portuguese).
        id (str): The ID of the president.

    Returns:
        dict: Details of the president with the given ID.

    Raises:
        KeyError: If the JSON file corresponding to the language is not found, or if the provided president ID does not exist.

    Examples:
        >>> search_all_presidents('en', '1') # doctest: +SKIP
        {
          "1": {
            "title": "President of Brazil 🇧🇷",
            "position": "1",
            "name": "Deodoro da Fonseca",
            "photo": "https://pt.wikipedia.org/wiki/Ficheiro:Deodoro_da_Fonseca_(1889).jpg",
            "broken": "none",
            "year_of_office": "November 15, 1889 – November 23, 1891 (2 years and 8 days)",
            "vice_president": "none",
            "local": "Brazil"
          }
        }
    """
    lang = lang.lower()

    if lang not in LANGUAGES:
        raise KeyError(f"Unsupported language: {lang}")

    if not (0 < int(id) <= 652):
        raise KeyError(
            "Provided president ID does not exist or is out of range")

    presidents_path = get_presidents_path()
    json_file = presidents_path / f"presidents-{lang}.json"

    with open(json_file, 'r', encoding='utf-8') as file:
        presidents_data = json.load(file)

    return presidents_data.get(id)

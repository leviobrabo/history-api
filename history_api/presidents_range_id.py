import json
from pathlib import Path

from history_api.plugins.languages import LANGUAGES


def get_presidents_path():
    return Path(__file__).resolve().parent / 'data' / 'presidents'


def get_presidents_range(lang: str, start_id: str, end_id: str) -> dict[str, dict[str, str]]:
    """
    Retrieves a range of presidents from start_id to end_id from a JSON file by language.

    Args:
        lang (str): The language code (e.g., 'pt' for Portuguese).
        start_id (str): The starting ID of the president range.
        end_id (str): The ending ID of the president range.

    Returns:
        dict: Dictionary containing presidents in the specified range for the provided language.
            The keys are the IDs and the values are president details.

    Raises:
        KeyError: If the provided president IDs are out of range.

    Examples:
      >>> search_all_presidents('en', '1', '2') # doctest: +SKIP
      {
                {
        "1": {
            "title": "President of Brazil 🇧🇷",
            "position": "1",
            "name": "Deodoro da Fonseca",
            "photo": "https://pt.wikipedia.org/wiki/Ficheiro:Deodoro_da_Fonseca_(1889).jpg",
            "broken": "none",
            "year_of_office": "November 15, 1889 – November 23, 1891 (2 years and 8 days)",
            "vice_president": "none",
            "local": "Brazil"
        },
        "2": {
            "title": "President of Brazil 🇧🇷",
            position: "2",
            "name": "Floriano Peixoto",
            "photo": "https://pt.wikipedia.org/wiki/Ficheiro:Floriano_Peixoto_(1891).jpg",
            "broken": "none",
            "year_of_office": "November 23, 1891 – November 15, 1894 (2 years and 357 days)",
            "vice_president": "none",
            "local": "Brazil"
        }
      }    
    """
    presidents_path = get_presidents_path()
    json_file = presidents_path / f"presidents-{lang}.json"

    lang = lang.lower()

    if lang not in LANGUAGES:
        raise KeyError(f"Unsupported language: {lang}")

    if not (0 < int(start_id) <= 652) or not (0 < int(end_id) <= 652):
        raise KeyError("Provided president IDs are out of range")

    with open(json_file, 'r', encoding='utf-8') as file:
        presidents_data = json.load(file)

    president_range = {}

    for president_id_str in range(int(start_id), int(end_id) + 1):
        if str(president_id_str) in presidents_data:
            president_range[str(president_id_str)
                            ] = presidents_data[str(president_id_str)]

    return president_range

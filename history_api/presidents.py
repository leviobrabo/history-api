import json
from pathlib import Path

from history_api.plugins.languages import LANGUAGES


def get_presidents_path():
    return Path(__file__).resolve().parent / 'data' / 'presidents'


def search_all_presidents(lang: str) -> dict[str, dict[str, str]]:
    """
    Searches for all presidents from a JSON file by language.

    Args:
        lang: The language of the presidents (e.g., 'en' for English).

    Returns:
        Dictionary containing all presidents for the provided language.

    Raises:
        FileNotFoundError: If the lang is not valid.

    Examples:
      >>> search_all_presidents('en') # doctest: +SKIP
      {
        "1": {
          "title": "President of Brazil 🇧🇷",
          position: "1",
          "name": "Deodoro da Fonseca",
          "photo": "https://pt.wikipedia.org/wiki/Ficheiro:Deodoro_da_Fonseca_(1889).jpg",
          "broken": "none",
          "year_of_office": "November 15, 1889 – November 23, 1891 (2 years and 8 days)",
          "vice_president": "none",
          "local": "Brazil"
        },
        # More ids...
        "652": {
          "title": "Prime Minister of South Africa 🇿🇦",
          position: "12",
          "name": "Cyril Ramaphosa",
          "photo": "https://pt.m.wikipedia.org/wiki/Ficheiro:Mr._Houlin_Zhao,_ITU_Secretary-General_with_H._E._Mr._Cyril_Ramaphosa,_President,_South_Africa_(cropped).jpg",
          "broken": "African National Congress",
          "year_of_office": "February 14, 2018 – present",
          "vice_president": "David Mabuza",
          "local": "South Africa"
        }
      }
    """
    lang = lang.lower()
    if lang not in LANGUAGES:
        raise FileNotFoundError(
            f"This language does not exist, available languages are: {list(LANGUAGES.keys())}")

    json_dir = get_presidents_path()
    json_file = json_dir / f"presidents-{lang}.json"

    with open(json_file, 'r', encoding='utf-8') as file:
        return json.load(file)

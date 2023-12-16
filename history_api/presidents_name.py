import json
from pathlib import Path

from history_api.plugins.languages import LANGUAGES


def get_presidents_path():
    return Path(__file__).resolve().parent / 'data' / 'presidents'


def get_president_by_name(lang, name):
    """
    Retrieves a president by name from a JSON file by language.

    Args:
        lang (str): The language code (e.g., 'pt' for Portuguese).
        name (str): The name of the president to search for.

    Returns:
        dict: Details of the president with the given name.

    Raises:
        FileNotFoundError: If the JSON file corresponding to the language is not found.
        ValueError: If the provided name does not match any president.

    Examples:
        >>> search_all_presidents('it', 'Yoon Suk-yeol') # doctest: +SKIP
            {
                "353": {
                "title": "Presidente della Corea del Sud Corea del Sud",
                "position": "13",
                "name": "Yoon Suk-yeol",
                "photo": "https://pt.wikipedia.org/wiki/Ficheiro:Yoon_Suk-yeol_in_May_2022.jpg",
                "broken": "potere delle persone",
                "year_of_office": "10 maggio 2022 - Titolare",
                "vice_president": "nessuno",
                "local": "South Korea"
                }
            }
    """
    lang = lang.lower()

    if lang not in LANGUAGES:
        raise FileNotFoundError(
            f"This language does not exist, available languages are: {list(LANGUAGES.keys())}")

    presidents_path = get_presidents_path()
    json_file = presidents_path / f"presidents-{lang}.json"

    with open(json_file, 'r', encoding='utf-8') as file:
        presidents_data = json.load(file)

    for details in presidents_data.values():
        president_name = details.get('name').lower()
        # Procura tanto o nome completo quanto o sobrenome na lista de presidentes
        if name.lower() in president_name:
            return details

    # Se nenhum presidente for encontrado correspondendo ao nome fornecido
    raise ValueError(f"President '{name}' is not available in the list.")

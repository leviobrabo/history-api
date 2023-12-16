import json
from pathlib import Path

from history_api.plugins.languages import LANGUAGES


def get_curiosity_path():
    return Path(__file__).resolve().parent / 'data' / 'curiosity'


def search_all_curiosity(lang: str) -> dict[str, list[str]]:
    """
        Searches for all curiosity from a JSON file by language.

        Args:
            lang: The language of the curiosity (e.g., 'pt' for Portuguese).

        Returns:
            Dictionary containing all curiosity for the provided language.

        Raises:
            FileNotFoundError: If the lang is not valid.

        Examples:
            >>> search_all_curiosity('pt') # doctest: +SKIP
            {
              "1-1": {
                "texto": "O Reino de Gana, localizado na África Ocidental, foi o primeiro grande império da região, conhecido por seu comércio de ouro e sal.",
                "texto1": "A África é o berço da humanidade, onde os primeiros seres humanos evoluíram."
              },
              "1-2": {
                "texto": "O Império Etíope foi uma das poucas nações africanas a resistir à colonização europeia durante o século XIX.",
                "texto1": "O Egito Antigo foi uma das civilizações mais avançadas da história, construindo as famosas pirâmides."
              },
                # More date-curiosity pairs...
                "12-31": {
                  "texto": "Em 31 de dezembro de 1759, o famoso compositor austríaco Wolfgang Amadeus Mozart nasceu em Salzburgo, deixando um legado duradouro na música clássica.",
                  "texto1": "No dia 31 de dezembro de 1999, ocorreu a virada do milênio, marcando o início do século XXI e o temido 'Bug do Milênio'q não causou os problemas catastróficos previstos em sistemas de computador em todo o mundo."
                }
            }
      """
    lang = lang.lower()
    if lang not in LANGUAGES:
        raise FileNotFoundError(
            f"This language does not exist, available languages are: {list(LANGUAGES.keys())}")

    json_dir = get_curiosity_path()
    json_file = json_dir / f"curiosity-{lang}.json"

    with open(json_file, 'r', encoding='utf-8') as file:
        return json.load(file)

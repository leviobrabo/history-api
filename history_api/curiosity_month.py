import json
from pathlib import Path

from history_api.plugins.languages import LANGUAGES


def get_curiosity_path():
    return Path(__file__).resolve().parent / 'data' / 'curiosity'


def search_curiosity_month(lang: str, month: str) -> dict[str, list[str]]:
    """
    Searches for all curiosity in a month from a JSON file by language.

    Args:
        lang (str): The language of the curiosity (e.g., 'pt' for Portuguese).
        month (str): The desired month number in the 'M' format.

    Returns:
        dict: Dictionary containing curiosity for the provided month in the 'M-D' format
              and the value is a list of curiosity for that date.

    Raises:
        ValueError: If the lang is not valid or if the month is not a number between 1 and 12.

    Examples:
        >>> search_curiosity_month('pl', '5') # doctest: +SKIP
        {
            "8-1": {
                "curiosity": [
                  {
                    "text": "1 sierpnia 1291 roku miało miejsce utworzenie Konfederacji Szwajcarskiej, kiedy trzy kantony połączyły się w pakcie o wzajemnej obronie, wyznaczając początek narodu szwajcarskiego."
                  },
                  {
                    "text1": "1 sierpnia 1944 roku miało miejsce Powstanie Warszawskie, powstanie przeciwko okupacji hitlerowskiej stolicy Polski podczas II wojny światowej."
                  }
                ]
              },
            "8-2": {
                "curiosity": [
                  {
                    "text": "2 sierpnia 1934 roku zmarł prezydent Niemiec Paul von Hindenburg, co pozwoliło Adolfowi Hitlerowi umocnić swoją władzę i zostać najwyższym przywódcą Niemiec."
                  },
                  {
                    "text1": "2 sierpnia 1990 r. Irak najechał Kuwejt, wywołując wojnę w Zatoce Perskiej i prowadząc do międzynarodowej interwencji pod przewodnictwem Stanów Zjednoczonych."
                  }
                ]
              },
            # More date-curiosity pairs...
            "8-31": {
              "curiosity": [
                {
                  "text": "31 sierpnia 1997 r. tragiczna śmierć księżnej Diany nastąpiła w wypadku samochodowym w Paryżu we Francji, wywołując zamieszanie na całym świecie i pozostawiając trwałe dziedzictwo jako działaczka humanitarna."
                },
                {
                  "text1": "31 sierpnia 1939 roku wraz z inwazją nazistowskich Niemiec na Polskę rozpoczęła się II wojna światowa, rozpoczynając globalny konflikt, który miał trwać sześć lat i pochłonąć miliony ofiar śmiertelnych."
                }
              ]
            },
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

    json_dir = get_curiosity_path()
    json_file = json_dir / f"curiosity-{lang}.json"
    curiosity_month = {}

    with open(json_file, 'r', encoding='utf-8') as file:
        curiosity = json.load(file)

        for key, value in curiosity.items():
            if key.startswith(f"{month}-"):
                curiosity_month[key] = value

        return curiosity_month

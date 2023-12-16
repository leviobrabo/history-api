import calendar
import json
from pathlib import Path

from history_api.plugins.languages import LANGUAGES


def get_events_path():
    return Path(__file__).resolve().parent / 'data' / 'events'


def search_events_month_day(lang: str, month: str, day: str) -> dict[str, list[str]]:
    """
    Searches for a specific event by date and language.

    Args:
        lang (str): The language of the events (e.g., 'pt' for Portuguese).
        month (str): The desired month number in the 'MM' format.
        day (str): The desired day number in the 'DD' format.

    Returns:
        list: List of events for the provided date in HTML format, if found, otherwise returns an empty list.

    Raises:
        ValueError: If the lang is not valid or if the month is not a number between 1 and 12.
        AssertionError: The day is not in the month parameter

    Examples:
        >>> search_events_month('fr', '12', '24') # doctest: +SKIP
        {
                "12-24": [
                    "[24/12/1524] • Vasco da Gama, navigateur portugais qui a découvert la route maritime des Indes, décède en Inde à l'âge de 64 ans.",
                    "[24/12/1779] • Créée au Portugal par D. Maria I, l'Académie Royale des Sciences de Lisbonne.",
                    "[24/12/1814] • La guerre de 1812 entre les États-Unis et la Grande-Bretagne se termine avec la signature du Traité de Gand par les deux pays.",
                    "[24/12/1908] • L'Opéra de Paris décide de sceller les enregistrements de grands musiciens sur l'un de ses murs, qui ne sera inauguré que 200 ans plus tard.",
                    "[24/12/1910] • Arrestation du caporal João Cândido, chef de la révolte des marins, et de 17 marins rebelles sur l'île Cobras.",
                    "[24/12/1919] • L'homme le plus riche du monde, John D. Rockefeller, fait un don de 100 millions de dollars à l'éducation et à d'autres causes philanthropiques.",
                    "[24/12/1934] • La première grève des postes et télégraphes a lieu au Brésil.",
                    "[24/12/1941] • Pendant la Seconde Guerre mondiale, la huitième armée britannique capture Benghazi, en Libye, aux forces allemandes.",
                    "[24/12/1951] • La Libye devient indépendante et proclame le retour à la monarchie sous le nom de Royaume-Uni de Libye.",
                    "[24/12/1951] • Getulio Vargas augmente le salaire minimum, gelé pendant huit ans, de 380 Cr$ à 1 200 Cr$."
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

    days_in_month = {
        1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    day = int(day)
    if day < 1 or day > days_in_month.get(month):
        month_name = calendar.month_name[month]
        raise AssertionError(
            f"Invalid day number for {month_name}. Please choose a day between 1 and {days_in_month.get(month)}.")

    json_dir = get_events_path()
    json_file = json_dir / f"events-{lang}.json"
    events_date = f"{month}-{day}"
    events_for_date = []

    if json_file.exists():
        with open(json_file, 'r', encoding='utf-8') as file:
            events = json.load(file)
            if events_date in events:
                events_for_date = events[events_date]

    return events_for_date

# History

## What's in the history API?

The History API provides historical event data for each day of the year, including:

-   **Events:** List of historical events of the day
-   **Presidents:** Details of 652 presidents from various countries, including the United States, China, Japan, Germany, India, United Kingdom, France, Brazil, Italy, Canada, South Korea, Russia, Australia, Spain, Mexico, Indonesia, Turkey, Argentina, Israel and South Africa.

-   **Births:** Significant figures in history born on each day of the year.

-   **Deaths:** Important historical figures who passed away on each day of the year.

-   **Historical Curiosities:** Interesting historical facts for each day of the year.

-   **Holidays:** Information about holidays for each day of the year.

-   **History Questions:** Four historical questions per day, each with four alternatives, one correct answer, and an explanation of up to 200 characters.

All this with support for 18 languages

## Installing

### To install the library, simply run the following command:

```bash
pip install history-api
```

### To install the development version, do the following:

```bash
git clone https://github.com/leviobrabo/history-api
```

## How to use?

Currently (2023), the History API uses functions and via the command line (CLI).

You can call events For example:

### Using modules and functions

This way, it will show all historical events with the language in Portuguese

```bash
import history-api

result = history_api.search_all_events('pt')  # Calling the function with a language example
print(result)  # Showing the result returned by the function
```

[For more examples on how to utilize the API, click here](https://seusite.com/Examples)

### Using the command line (CLI)

If you wanted to use it via the terminal command line, do this:

```bash
poetry run events
```

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Events                                                                                     ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ [1/1/1502] • Portuguese navigators arrived at the coast of the South American continent    │
│ and named the current city Rio de Janeiro.                                                 │
│ [1/1/1764] • In France, Wolfgang Amadeus Mozart, at the age of 8, plays the piano for the  │
│ Royal Family in Versailles.                                                                │
│ [1/1/1776] • The leader of the American Revolution, George Washington presents the first   │
│ national flag of the United States.                                                        │
│ [1/1/1797] • Albany replaces New York City as capital of the state of New York.            │
│ [1/1/1801] • The Act of Union, signed by Great Britain and Ireland, creates the United     │
│ Kingdom.                                                                                   │
│ [1/1/1804] • After leading a rebellion against the French, Jean-Jacques Dessalines         │
│ proclaims an independent Haiti.                                                            │
│ [1/1/1833] • The United Kingdom declares its sovereignty over the Falkland Islands.        │
│ [1/1/1877] • The English Queen Victoria is proclaimed Empress of India.                    │
│ [1/1/1942] • 26 nations sign the United Nations Declaration, expressing opposition to the  │
│ Axis Forces.                                                                               │
│ [1/1/1945] • France admitted to the United Nations.                                        │
└────────────────────────────────────────────────────────────────────────────────────────────┘
```

##### By default I set the language to English

```bash
poetry run events --help

╭─ Arguments ────────────────────────────────────────────────────────────────────────────────╮
│   lang       [LANG]   Language [default: en]                                               │
│   month      [MONTH]  Month [default: 1]                                                   │
│   day        [DAY]    Day [default: 1]                                                     │
╰────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Language

### Supported Languages

| Language Code | Language Name (English) |
| ------------- | ----------------------- |
| ar            | Arabic                  |
| cs            | Czech                   |
| de            | German                  |
| en            | English                 |
| es            | Spanish                 |
| fr            | French                  |
| hi            | Hindi                   |
| id            | Indonesian              |
| it            | Italian                 |
| ja            | Japanese                |
| ko            | Korean                  |
| pl            | Polish                  |
| pt            | Portuguese              |
| ru            | Russian                 |
| tr            | Turkish                 |
| uk            | Ukrainian               |
| vi            | Vietnamese              |
| zh            | Chinese                 |

### Correct or add translation?

#### Add Translation

##### Procedure

1. Check if the language (lang) already exists.
2. Locate the source file in the project for "en" (English) in the desired scope:
    - Events Scope: [events-en.json](https://github.com/leviobrabo/history-api/blob/main/history_api/data/events/events-en.json)
    - Presidents Scope: [presidents-en.json](https://github.com/leviobrabo/history-api/blob/main/history_api/data/presidents/presidents-en.json)
3. Send a pull request (PR) with the translation file following the model:
    - `{scope}-{lang}.json`
        - Scope: events or presidents
        - Lang: The language you chose.
4. [Create a PR here](https://github.com/leviobrabo/history-api/pulls)

#### Correct Translation

##### Procedure

1. Check the language you want to correct.
2. Go to the source and find the corresponding file for the language.
3. Make necessary alterations and corrections.
4. Submit a PR [here](https://github.com/leviobrabo/history-api/pulls)

##### Instructions

-   Ensure to follow the structure of the existing file.
-   Maintain consistency in format, structure, and content.

##### Additional Notes

-   When submitting a PR, add a clear description of the changes made.
-   Be diligent in providing a clear and accurate translation.

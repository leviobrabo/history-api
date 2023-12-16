## How to use?

Currently (2023), the History API uses functions and via the command line (CLI).

You can call events For example:

### Using modules and functions

This way, it will show all historical events with the language in Portuguese

```py
import history-api

result = history_api.search_all_events('pt')  # Calling the function with a language example
print(result)  # Showing the result returned by the function
```

['For more examples on how to utilize the API, click here'][For more examples on how to utilize the API, click here]

[For more examples on how to utilize the API, click here]: /examples/#Examples

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

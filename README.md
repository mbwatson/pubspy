# PubsPy

## What this Accomplishes

Utilizes the [Crossref API](https://api.crossref.org/) to turn a list of [DOI](https://www.doi.org/)s into a list of publication objects. See the example below.

## Example

Read a file, such as the following, to ingest a list of DOIs.

```json
[
  "10.5479/sil.52126.39088015628399",
  "10.1037/13681-000",
  "10.1007/978-1-4615-9763-6"
]
```

Output a list of publication objects, like the following.

```json
[
  {
    "doi": "10.5479/sil.52126.39088015628399",
    "title": [
      "Philosophiae naturalis principia mathematica"
    ],
    "authors": [
      "Isaac Newton"
    ],
    "type": "monograph",
    "container": [],
    "date": "2016-07-25",
    "citation": "Newton, I. (1687). Philosophiae naturalis principia mathematica. doi:10.5479/sil.52126.39088015628399\n"
  },
  {
    "doi": "10.1037/13681-000",
    "title": [
      "The origin of species: By means of natural selection or the preservation of favoured races in the struggle for life."
    ],
    "authors": [
      "Charles Darwin"
    ],
    "type": "book",
    "container": [],
    "date": "2012-02-13",
    "citation": "Darwin, C. (1906). The origin of species: By means of natural selection or the preservation of favoured races in the struggle for life. doi:10.1037/13681-000\n"
  },
  {
    "doi": "10.1007/978-1-4615-9763-6",
    "title": [
      "Enumerative Combinatorics"
    ],
    "authors": [
      "Richard P. Stanley"
    ],
    "type": "book",
    "container": [],
    "date": "2013-12-26",
    "citation": "Stanley, R. P. (1986). Enumerative Combinatorics. doi:10.1007/978-1-4615-9763-6\n"
  }
]
```

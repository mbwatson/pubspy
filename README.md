# PubsPy

## What this Accomplishes

Utilizes the [Crossref API](https://api.crossref.org/) to turn a list of [DOI](https://www.doi.org/)s into a list of publication objects. See the example below.

## How to Use

Define a way to get a list of DOIs into the `build.py` script. A simple way is to have a `dois.json` file and have python read it directly. This is the method assumed and currently coded in `build.py`, but of course other methods can work--read a plain text file, query a database, hit an API endpoint, etc.

Once the DOIs are in the `dois` variable, we define a Library instance, build the library (contains Publication objects), and write it to a JSON file, specified by the `PUBLICATIONS_FILE` variable.

```python
library = Library()
library.build(dois)
library.write(PUBLICATIONS_FILE)
```

## Example

Read a file, such as the following, to ingest a list of DOIs.

```json
[
  "10.5479/sil.52126.39088015628399",
  "10.1037/13681-000"
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
  }
]
```

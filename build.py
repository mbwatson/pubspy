from library import Publication, Library
import json

#

def read_dois(filename, count = None):
    # Read list of DOIs
    try:
        assert type(count) is int or count == None
        with open(filename) as f:
            if count:
                dois = json.load(f)[:count]
            else:
                dois = json.load(f)
    except AssertionError:
        print('Error read_dois: <count> must be of type \'int\' if set.')
        return []
    return dois

DOI_FILE = './dois.json'
PUBLICATIONS_FILE = './library.json'

#

dois = read_dois(DOI_FILE, 3)
library = Library()
library.build(dois)
library.write(PUBLICATIONS_FILE)
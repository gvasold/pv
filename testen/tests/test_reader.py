
import csv
from cities import read_csv

TESTDATA = [
                {"Stadt": "Linz", "Bezirk": "Linz", "Bundesland": "Upper Austria", "Einwohner": 204846},
                {"Stadt": "Graz", "Bezirk": "Graz", "Bundesland": "Styria", "Einwohner": 287723}
        ]


def test_read_csv():
    "Test case: Read csv file with two rows of data"
    # generate a test csv file
    with open('test.csv', 'w', newline='', encoding='utf-8') as fh:
        writer = csv.DictWriter(fh, fieldnames=TESTDATA[0].keys())
        writer.writeheader()
        writer.writerows(TESTDATA)
    assert read_csv('test.csv') == TESTDATA

def test_empty_csv():
    "Test case: Empty csv file"
    filename = 'test.csv'
    with open("test.csv", "w", newline='', encoding='utf-8') as fh:
        writer = csv.DictWriter(fh, fieldnames=['Stadt', 'Bezirk', 'Bundesland', 'Einwohner'])
        writer.writeheader( )
    assert read_csv(filename) == []

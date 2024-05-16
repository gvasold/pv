import csv
import os

from cities import filter_by_name, filter_by_population, read_csv

TESTDATA = [
    {"Stadt": "Graz", "Bezirk": "Graz", "Bundesland": "Styria", "Einwohner": 287723},
    {
        "Stadt": "Linz",
        "Bezirk": "Linz",
        "Bundesland": "Upper Austria",
        "Einwohner": 204846,
    },
    
]


def test_read_csv():
    "Test case: Read csv file with two rows of data"
    # generate a test csv file
    with open("test.csv", "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=TESTDATA[0].keys())
        writer.writeheader()
        writer.writerows(TESTDATA)
    assert read_csv("test.csv") == TESTDATA
    os.remove("test.csv")


def test_empty_csv():
    "Test case: Empty csv file"
    filename = "test.csv"
    with open("test.csv", "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh, fieldnames=["Stadt", "Bezirk", "Bundesland", "Einwohner"]
        )
        writer.writeheader()
    assert read_csv(filename) == []
    os.remove("test.csv")


def test_filter_by_name_case_sensitive():
    "Test case: Filter by name (case sensitive)"
    assert filter_by_name(TESTDATA, "linz", case_sensitive=True) == []
    assert filter_by_name(TESTDATA, "Linz", case_sensitive=True) == [
        {
            "Stadt": "Linz",
            "Bezirk": "Linz",
            "Bundesland": "Upper Austria",
            "Einwohner": 204846,
        }
    ]
    assert filter_by_name(TESTDATA, "in", case_sensitive=True) == [
        {
            "Stadt": "Linz",
            "Bezirk": "Linz",
            "Bundesland": "Upper Austria",
            "Einwohner": 204846,
        }
    ]


def test_filter_by_name_case_insensitive():
    "Test case: Filter by name (case sensitive)"
    assert filter_by_name(TESTDATA, "linz", case_sensitive=False) == [
        {
            "Stadt": "Linz",
            "Bezirk": "Linz",
            "Bundesland": "Upper Austria",
            "Einwohner": 204846,
        }
    ]
    assert filter_by_name(TESTDATA, "Linz") == [
        {
            "Stadt": "Linz",
            "Bezirk": "Linz",
            "Bundesland": "Upper Austria",
            "Einwohner": 204846,
        }
    ]
    assert filter_by_name(TESTDATA, "in") == [
        {
            "Stadt": "Linz",
            "Bezirk": "Linz",
            "Bundesland": "Upper Austria",
            "Einwohner": 204846,
        }
    ]
    assert filter_by_name(TESTDATA, "inn") == []


def test_filter_by_population():
    "Test case: Filter by population"
    assert filter_by_population(TESTDATA, 250000) == [
        {"Stadt": "Graz", "Bezirk": "Graz", "Bundesland": "Styria", "Einwohner": 287723}
    ]


if __name__ == "__main__":
    test_read_csv()
    test_empty_csv()
    test_filter_by_name_case_sensitive()
    test_filter_by_population()
    print("All tests passed.")

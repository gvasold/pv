import pytest
import tempfile

import os
import csv

@pytest.fixture
def tmpdir():
    "Yield the path to a temporary directory."
    with tempfile.TemporaryDirectory() as tmpdirpath:
        yield tmpdirpath

@pytest.fixture
def testdata():
    "Return a list of test data."
    return [
        {
            "Stadt": "Linz",
            "Bezirk": "Linz",
            "Bundesland": "Upper Austria",
            "Einwohner": 204846,
        },
        {"Stadt": "Graz", "Bezirk": "Graz", "Bundesland": "Styria", "Einwohner": 287723},
    ]        

@pytest.fixture
def testcsv(tmpdir, testdata):
    "Generate a test csv file."
    csv_file = os.path.join(tmpdir, "test.csv")
    with open(csv_file, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=testdata[0].keys())
        writer.writeheader()
        writer.writerows(testdata)
    return csv_file

@pytest.fixture
def emptycsv(tmpdir):
    "Generate an empty csv file."
    csv_file = os.path.join(tmpdir, "test.csv")
    with open(csv_file, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh, fieldnames=["Stadt", "Bezirk", "Bundesland", "Einwohner"]
        )
        writer.writeheader()
    return csv_file
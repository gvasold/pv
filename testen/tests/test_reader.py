import csv
import tempfile

import pytest

from cities import read_csv

TESTDATA = [
    {
        "Stadt": "Linz",
        "Bezirk": "Linz",
        "Bundesland": "Upper Austria",
        "Einwohner": 204846,
    },
    {"Stadt": "Graz", "Bezirk": "Graz", "Bundesland": "Styria", "Einwohner": 287723},
]


@pytest.fixture
def tmpdir():
    with tempfile.TemporaryDirectory() as tmpdirpath:
        yield tmpdirpath


def test_read_csv(tmpdir):
    "Test case: Read csv file with two rows of data"
    # generate a test csv file
    csv_file = os.path.join(tmpdir, "test.csv")
    with open(csv_file, newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=TESTDATA[0].keys())
        writer.writeheader()
        writer.writerows(TESTDATA)
    assert read_csv("test.csv") == TESTDATA


def test_empty_csv(tmpdir):
    "Test case: Empty csv file"
    csv_file = os.path.join(tmpdir, "test.csv")
    with open(csv_file, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh, fieldnames=["Stadt", "Bezirk", "Bundesland", "Einwohner"]
        )
        writer.writeheader()
    assert read_csv(csv_file) == []

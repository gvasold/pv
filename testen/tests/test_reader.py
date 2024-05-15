from cities import read_csv


def test_read_csv(testcsv, testdata):
    "Test case: Read csv file with two rows of data"
    assert read_csv(testcsv) == testdata


def test_empty_csv(emptycsv):
    "Test case: Empty csv file"
    assert read_csv(emptycsv) == []

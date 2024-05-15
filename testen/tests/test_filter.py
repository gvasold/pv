from cities import filter_by_name, filter_by_population


def test_filter_by_name_case_sensitive(testdata):
    "Test case: Filter by name (case sensitive)"
    assert filter_by_name(testdata, "linz", case_sensitive=True) == []
    assert filter_by_name(testdata, "Linz", case_sensitive=True) == [
        testdata[0]
    ]  # Linz
    assert filter_by_name(testdata, "in", case_sensitive=True) == [testdata[0]]  # Linz
    assert filter_by_name(testdata, "inn", case_sensitive=True) == []


def test_filter_by_name_case_insensitive(testdata):
    "Test case: Filter by name (case sensitive)"
    assert filter_by_name(testdata, "linz", case_sensitive=False) == [
        testdata[0]
    ]  # Linz
    assert filter_by_name(testdata, "Linz") == [testdata[0]]  # Linz
    assert filter_by_name(testdata, "in") == [testdata[0]]  # Linz
    assert filter_by_name(testdata, "inn") == []


def test_filter_by_population(testdata):
    "Test case: Filter by population"
    assert filter_by_population(testdata, 100000) == testdata
    assert filter_by_population(testdata, 250000) == [testdata[1]]  # Graz
    assert filter_by_population(testdata, 300000) == []

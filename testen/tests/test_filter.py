from cities import filter_by_name, filter_by_population


TESTDATA = [
    {
        "Stadt": "Linz",
        "Bezirk": "Linz",
        "Bundesland": "Upper Austria",
        "Einwohner": 204846,
    },
    {"Stadt": "Graz", "Bezirk": "Graz", "Bundesland": "Styria", "Einwohner": 287723},
]


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
    assert filter_by_population(TESTDATA, 200000) == [
        {"Stadt": "Graz", "Bezirk": "Graz", "Bundesland": "Styria", "Einwohner": 287723}
    ]

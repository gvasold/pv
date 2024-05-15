import unittest
from cities import read_csv, filter_by_name, filter_by_population

class TestCities(unittest.TestCase):
    def setUp(self):
        self.cities = [
            {'Stadt': 'Berlin', 'Bezirk': 'Mitte', 'Bundesland': 'Berlin', 'Einwohner': '3769495'},
            {'Stadt': 'Hamburg', 'Bezirk': 'Hamburg-Mitte', 'Bundesland': 'Hamburg', 'Einwohner': '1841179'},
            {'Stadt': 'Munich', 'Bezirk': 'Munich', 'Bundesland': 'Bavaria', 'Einwohner': '1471508'},
            {'Stadt': 'Cologne', 'Bezirk': 'Cologne', 'Bundesland': 'North Rhine-Westphalia', 'Einwohner': '1085664'},
            {'Stadt': 'Frankfurt', 'Bezirk': 'Frankfurt', 'Bundesland': 'Hesse', 'Einwohner': '753056'}
        ]

    def test_read_csv(self):
        expected = [
            {'Stadt': 'Berlin', 'Bezirk': 'Mitte', 'Bundesland': 'Berlin', 'Einwohner': 3769495},
            {'Stadt': 'Hamburg', 'Bezirk': 'Hamburg-Mitte', 'Bundesland': 'Hamburg', 'Einwohner': 1841179},
            {'Stadt': 'Munich', 'Bezirk': 'Munich', 'Bundesland': 'Bavaria', 'Einwohner': 1471508},
            {'Stadt': 'Cologne', 'Bezirk': 'Cologne', 'Bundesland': 'North Rhine-Westphalia', 'Einwohner': 1085664},
            {'Stadt': 'Frankfurt', 'Bezirk': 'Frankfurt', 'Bundesland': 'Hesse', 'Einwohner': 753056}
        ]
        result = read_csv('cities.csv')
        self.assertEqual(result, expected)

    def test_filter_by_name_case_sensitive(self):
        expected = [
            {'Stadt': 'Hamburg', 'Bezirk': 'Hamburg-Mitte', 'Bundesland': 'Hamburg', 'Einwohner': 1841179},
            {'Stadt': 'Frankfurt', 'Bezirk': 'Frankfurt', 'Bundesland': 'Hesse', 'Einwohner': 753056}
        ]
        result = filter_by_name(self.cities, 'burg', case_sensitive=True)
        self.assertEqual(result, expected)

    def test_filter_by_name_case_insensitive(self):
        expected = [
            {'Stadt': 'Hamburg', 'Bezirk': 'Hamburg-Mitte', 'Bundesland': 'Hamburg', 'Einwohner': 1841179},
            {'Stadt': 'Cologne', 'Bezirk': 'Cologne', 'Bundesland': 'North Rhine-Westphalia', 'Einwohner': 1085664},
            {'Stadt': 'Frankfurt', 'Bezirk': 'Frankfurt', 'Bundesland': 'Hesse', 'Einwohner': 753056}
        ]
        result = filter_by_name(self.cities, 'burg', case_sensitive=False)
        self.assertEqual(result, expected)

    def test_filter_by_population(self):
        expected = [
            {'Stadt': 'Cologne', 'Bezirk': 'Cologne', 'Bundesland': 'North Rhine-Westphalia', 'Einwohner': 1085664},
            {'Stadt': 'Frankfurt', 'Bezirk': 'Frankfurt', 'Bundesland': 'Hesse', 'Einwohner': 753056}
        ]
        result = filter_by_population(self.cities, 1000000)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
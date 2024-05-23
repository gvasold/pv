import csv
import os.path
import tempfile
import unittest
from cities import read_csv, filter_by_name, filter_by_population

class TestCities(unittest.TestCase):
    def setUp(self):
        self.cities = [
            {'Stadt': 'Foo', 'Bezirk': 'Foobezirk', 'Bundesland': 'Fooland', 'Einwohner': 100},
            {'Stadt': 'Bar', 'Bezirk': 'Barbezirk', 'Bundesland': 'Barland', 'Einwohner': 200},
            {'Stadt': 'Foo Bar', 'Bezirk': 'Foobarbezirk', 'Bundesland': 'Foobarland', 'Einwohner': 300},
        ]

    def test_read_csv(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            filename = os.path.join(tmpdirname, 'cities.csv')
            with open(filename, 'w') as fh:
                writer = csv.DictWriter(fh, fieldnames=['Stadt', 'Bezirk', 'Bundesland', 'Einwohner'])
                writer.writeheader()
                writer.writerows(self.cities)
            result = read_csv(filename)
            
            self.assertEqual(len(result), 3)
            self.assertEqual(result[0]['Stadt'], 'Foo')
            self.assertEqual(result[1]['Stadt'], 'Bar')
            self.assertEqual(result[2]['Stadt'], 'Foo Bar')

            # Test if Einwohner is an integer
            self.assertEqual(result[0]['Einwohner'], 100)

    def test_filter_by_name_case_sensitive(self):
        "Test filter_by_name with case_sensitive=True"
        result = filter_by_name(self.cities, 'Foo', case_sensitive=True)
        self.assertEquals(len(result), 2)
        self.assertEquals('Foo', result[0]['Stadt'])
        self.assertEquals('Foo Bar', result[1]['Stadt'])

        result = filter_by_name(self.cities, 'foo', case_sensitive=True)
        self.assertEquals(len(result), 0)

        result = filter_by_name(self.cities, 'oo', case_sensitive=True)
        self.assertEquals(len(result), 2)
        self.assertEquals('Foo', result[0]['Stadt'])
        self.assertEquals('Foo Bar', result[1]['Stadt'])

        result = filter_by_name(self.cities, '00', case_sensitive=True)
        self.assertEquals(len(result), 0)


    def test_filter_by_name_case_insensitive(self):
        "Test filter_by_name with case_insensitive=True"
        result = filter_by_name(self.cities, 'Foo', case_sensitive=False)
        self.assertEquals(len(result), 2)
        self.assertEquals('Foo', result[0]['Stadt'])
        self.assertEquals('Foo Bar', result[1]['Stadt'])

        result = filter_by_name(self.cities, 'foo', case_sensitive=False)
        self.assertEquals(len(result), 2)
        self.assertEquals('Foo', result[0]['Stadt'])
        self.assertEquals('Foo Bar', result[1]['Stadt'])

        result = filter_by_name(self.cities, 'oo', case_sensitive=False)
        self.assertEquals(len(result), 2)
        self.assertEquals('Foo', result[0]['Stadt'])
        self.assertEquals('Foo Bar', result[1]['Stadt'])

        result = filter_by_name(self.cities, '00', case_sensitive=True)
        self.assertEquals(len(result), 0)


    def test_filter_by_population(self):
        "Test filter_by_population"
        result = filter_by_population(self.cities, 300)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['Stadt'], 'Foo Bar')

        result = filter_by_population(self.cities, 1000)
        self.assertEqual(len(result), 0)

        result = filter_by_population(self.cities, 0)
        self.assertEqual(len(result), 3)

        result = filter_by_population(self.cities, -99)
        self.assertEqual(len(result), 3)


if __name__ == '__main__':
    unittest.main()
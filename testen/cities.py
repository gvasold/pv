import csv
from typing import Dict, List


def read_csv(filename: str) -> List[Dict[str, str]]:
    """
    Read the csv file `filename` and yield each row as dict.

    The keys of the dict are the column names of the csv file:
    'Stadt', 'Bezirk', 'Bundesland', 'Einwohner'.
    """
    cities = []
    with open(filename, "r", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            row["Einwohner"] = int(row["Einwohner"].replace(".", ""))
            cities.append(row)
    return cities


def filter_by_name(
    cities: "List[Dict[str, str]]", needle: str, case_sensitive=False
) -> List[Dict[str, str]]:
    """
    Return only rows where the city name contains the string `needle`.
    """
    result = []
    for row in cities:
        if case_sensitive:
            if needle in row["Stadt"]:
                result.append(row)
        else:
            if needle.lower() in row["Stadt"].lower():
                result.append(row)
    return result


def filter_by_population(
    cities: "list[dict[str, str]]", min_population
) -> List[Dict[str, str]]:
    """
    Return only rows where population is greater equals min_polulation.
    """
    result = []
    for row in cities:
        if row["Einwohner"] >= min_population:
            result.append(row)
    return result


if __name__ == "__main__":
    data = read_csv("cities.csv")
    filtered_data = filter_by_name(data, "a")
    filtered_data = filter_by_population(filtered_data, 10000)
    filtered_data.sort(key=lambda x: (x["Bundesland"], x["Stadt"]))
    for row in filtered_data:
        print(row)

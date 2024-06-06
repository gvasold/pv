"""This is a simple module, which is used to demonstrate how the
load_data function can be mocked or patched when running tests.
"""

from unittest.mock import MagicMock


def load_data(filename):
    with open(filename) as fh:
        data = [int(line.strip()) for line in fh]
    return data


def analyze_data(filename):
    data = load_data(filename)
    return sum([val for val in data if val > 10])



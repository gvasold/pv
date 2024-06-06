"""This module shows, how we can replace a module function with a Mock object.
In module foo_mm the function analyze_data() uses another function load_data(),
which reads from a file. For testing it would be much easier, if the 
load_data() function would return any value we want without the need to
create a temporary data file.
"""


from unittest.mock import MagicMock
import foo_mm


def test_analyze():
    # we override the load_data function with a mock
    foo_mm.load_data = MagicMock()
    foo_mm.load_data.return_value = [1, 11, 15, 3]
    assert foo_mm.analyze_data('foofoo') == 26

if __name__ == '__main__':
    test_analyze()
    print('Test passed')

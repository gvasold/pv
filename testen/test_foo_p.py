"""This is an example on how to reach the same thing as in 
test_foo_mm.py, but this time we use the patch decorator,
which automatically adds a local mock_xxx variable, representing
the patched function/method
"""

from unittest.mock import patch

import foo_mm


@patch('foo_mm.load_data')
def test_analyze(mock_read):
    mock_read.return_value = [1, 11, 15, 3]
    assert foo_mm.analyze_data('foofoo') == 26

if __name__ == '__main__':
    test_analyze()
    print('Test passed')

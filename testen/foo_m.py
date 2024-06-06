"""This small example demonstrates how we can replace an object with a 
mock.
We create a mock object and fake a some_method() method with a fixed return
value.
"""
from unittest.mock import Mock


foo = Mock()
foo.some_method.return_value = "42"

print(foo.some_method())


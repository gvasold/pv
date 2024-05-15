# Some tests demonstrating how to test a class
from person import Person
import pytest
import datetime

@pytest.fixture
def testperson():
    "Return a Person object."
    return Person("Max", "Mustermann", "2000-01-01")

def test_init_date_as_str():
    "Test the __init__ method using a string as birthday."
    testperson = Person("Max", "Mustermann", "2000-01-01")
    assert testperson.firstname == "Max"
    assert testperson.lastname == "Mustermann"
    assert testperson.birthday == datetime.date(2000, 1, 1)

def test_init_date_as_date():
    "Test the __init__ method using a datetime.date object as birthday."
    birthday = datetime.date(2000, 1, 1)
    testperson = Person("Max", "Mustermann", birthday)
    assert testperson.firstname == "Max"
    assert testperson.lastname == "Mustermann"
    assert testperson.birthday == datetime.date(2000, 1, 1)  

def test_name(testperson):
    "Test the name property."
    assert testperson.name == "Mustermann, Max"

def test_get_age(testperson): 
    "Test the get_age method."
    assert testperson.get_age(datetime.date(2021, 2, 3)) == 21   


def test_recreate1(testperson):
    """This is not a real test.
    It demonstrates, that each function gets a fresh testperson object.
    """
    # we change the firstname of the testperson object
    testperson.firstname = "Hans"
    assert testperson.firstname == "Hans"
    
def test_recreate2(testperson):
    """This is not a real test.
    It demonstrates, that each function gets a fresh testperson object.
    """
    # We changed the firstname property in the previous test.
    # But as each test function gets a fresh testperson object, the firstname is "Max" again.
    assert testperson.firstname == "Max"
          
# pv
Repository for the "Programmieren vertieft" course.

## Topic: Testing

The purpose of the testing directory and all branches starting with 'testen-' is 
to demonstrate different (and improved) ways to test code.

### Branch testen-1

This branch contains `simpletests.py` containing simple tests without using 
a test framework. This is only to demonstrate the core idea of automated tests.
Normally you would always prefer to use a test framework like shown in the other 
branches.

### Branch testen-2

This branch shows how to use the unittest Framework contained in the 
standard library. Personally, like most Python developers, I prefer 
the pytest framwork over the unittest framework.

The big difference to testen-1 is, the we use the unittest framework 
(which is heavily inspired by the junit Framework fpr Java). The framwork 
provides some test classes and assertion methods. It also contains a test 
runner, which is able to collect tests from different files, run these and
presents the outcome.

### Branch testen-3a

This branch uses the pytest framework. As it is not part of the standard 
library, there is a chance that you have to install it (pip install pytest).

This branch uses the framework in a very minimalistic way. All test modules
are stored in a `tests` folder, which ist not strictly necessary, but a good
practice. Notice that I put two test modules there which do not follow a common
naming scheme: `filter_test.py` and `test_reader.py`. Normally you would settle
on either `test_xxx.py` or `xxx_test.py`. To have `test_` or `_test.py` in the
file name is very important, because this is how the pytest test collector 
identifies test modules to run.

### Branch testen-3b

This branch improves the pytest based tests in a first step:

  * it unifies the names schema of the test files
  * it moves the ugly test csv files to a temporary directory. This also 
    demonstrates how to use pytest fixtures, a very powerful alternative
    to unittests setup() method

### Branch testen-3c

  * Create a conftest.py module. All fixtures defined in this module can be used 
    directly in any test module 
  * Move the test data to fixture functions in the conftest.py file.
    The advantage of this is, that this data will be recreated by default for 
    each test function - it is very important, that a test function cannot 
    influence other test functions. Using a fixture for test data creation (or 
    anything else which has might be changed by tests) solves this problem.
    Do not get confused: Here this is not really necessary, as the data is 
    never changed during tests, but I take it as an example to show how to create 
    data in fixtures.

### Branch testen-3d

  * This branch contains a new example person.py and test_person.py. It demonstrates 
    how to test a class.
  * Add the end of test_person.py I have added a small example to show how using a fixture
    guarantees, that the Person object is recreated for each test function (test_recreate1 
    and test_recreate2).

#### Coverage
In branch-3d we could also test the coverage function. Coverage means, that we get information
about the percentage of code which is tested.

To use this functionality, we must install a pytest plugin called pytest-cov (``pip install pytest-cov``)

Then we can run this command:

```
pytest --cov
```

To find out which parts of the code are not tested, we use this command:

```
pytest --cov --cov-report=term-missing
```

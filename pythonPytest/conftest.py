# Importing the Pytest library
import pytest

# Creating the common function for input
@pytest.fixture
def input_value():
    c = 8
    return c

# Importing the math library
import math

# Creating first test case
def test_check_floor(input_value):
    assert input_value==math.floor(8.34532)

# Creating second test case
def test_check_equal(input_value):
    assert 5 == input_value

# Creating first test case
def test_check_difference(input_value):
    assert 99-93==input_value

# Creating second test case
def test_check_square_root(input_value):
    assert input_value==math.sqrt(64)

# All functions taken from "Python Numerical Methods", Kong, Siauw and Bayen
# https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html

import pytest
from adder.py import my_adder

#test function

#@pytest.mark.parametrize("test_input, expected", ["1,1,1", 3])

def test_adder():
	assert my_adder(1,1,1) == 3
	assert my_adder("apple", "banana", "orange") == "apple"+"banana"+"orange"



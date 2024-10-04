# All functions taken from "Python Numerical Methods", Kong, Siauw and Bayen
# https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html

import pytest
from adder import my_adder

def test_adder():
	assert my_adder(1,1,1) == 3
	assert my_adder("apple", "banana", "orange") == "apple"+"banana"+"orange"



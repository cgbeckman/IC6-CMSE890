import pytest 
from example_functions import have_digits

def test_digits():
	assert have_digits("hello") == 0
	assert have_digits("goodbye") == 0
	assert have_digits("Hello 2") == 0



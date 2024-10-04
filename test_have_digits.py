import pytest 
from have_digits import have_digits

def test_digits():
	assert have_digits("hello") == 0
	assert have_digits("goodbye") == 0
	



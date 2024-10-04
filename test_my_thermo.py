import pytest 
from thermostat import my_thermo_stat

def test_my_thermo():
	assert my_thermo_stat(85, 99) == 'Heat'
	assert my_thermo_stat(67, 66) == 'off'
	assert my_thermo_stat(99, 80) == 'AC'



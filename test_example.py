# Tests from https://www.softwaretestinghelp.com/pytest-tutorial/
from area_function import area_function
from perimeter_function import perimeter_function
import pytest

@pytest.mark.parametrize("width,height,area", [(3, 5, 15), (2, 4, 8), (6, 9, 54)])
def test_area(width, height, area):
    output = area_function(width, height)
    assert output == area

@pytest.mark.parametrize("width,height,perimeter", [(3, 5, 16), (2, 4, 12), (6, 9, 30)])
def test_perimeter(width, height, perimeter):
    output = perimeter_function(width,height)
    assert output == perimeter
    

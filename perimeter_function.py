def perimeter_function(w : float | int,h : float | int) -> float | int:
    """
    This function computes the perimeter of a rectangle according to the following equation: 2*width + 2*height = perimeter.
    
    -------------
    |           | height 
    -------------
    width

    Args:
         w: the width of the rectangle 
         h: the height of the rectangle
    Returns:
            The perimeter of the rectangle
    Authors:
            Made by Andrew Fullard
            Edited by Cate Beckman for CMSE 890
    """
    perimeter = 2*w+2*h
    return perimeter

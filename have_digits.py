def have_digits(s : int):
    """	
    This function checks if a string has digits in it
    
    Args:
         s: the string you would like to check 
    Returns: 
	    Breaks if a character in s is a digit
    Authors:
            Made by Andrew Fullard 
            Edited by Cate Beckman for CMSE 890
    """

    out = 0
    
    # loop through the string
    for c in s:
        # check if the character is a digit
        if c.isdigit():
            out = 1
            break 
       
    return out

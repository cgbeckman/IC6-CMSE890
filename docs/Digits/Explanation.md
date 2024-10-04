# Digits Explanation 

This function checks if a string has digits in it.

Args:<ul>
         <li>s: the string you would like to check, string</li>
</ul>    
Returns:<ul>
            <li>Breaks if a character in s is a digit. Returns number of digits as int.</li>
</ul>
Authors:<ul>
            <li>Made by Andrew Fullard</li>
            <li>Edited by Cate Beckman for CMSE 890</li>
</ul>

## Code

```def have_digits(s : int):
        out = 0
        for c in s:
        if c.isdigit():
            out = 1
            break
        return out```


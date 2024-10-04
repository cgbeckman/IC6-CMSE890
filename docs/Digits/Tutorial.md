# Tutorial for Digits Function

This page gives a tutorial for how to check the string "hello 2x" for digits. Below are two tutorials, one 
using a python interface, the other using command line. 

# Tutorial for using a python interface.
1.  Open VSCode, Conda, or preferred code editor.
2.  Open a blank script.
3.  Import digits.py into the script with the line: from digits import have_digits
4.  We will call the function to check the string "hello 2x". Call the function with the line: output=have_digits(hello 2x)
5.  Add a line to check the output: print("Output: ", output)
6.  Run the script

The output should read "1", because there is 1 digit in the phrase "hello 2x". If it does not, check the string was input 
correctly.

# Tutorial for command line
1. Open command line/terminal
2. Go to the directory where the function have_digits is stored.
3. Import the function with the line: from digits import have_digits
4. Open python by entering "python" in command line. Hit enter. A new line should show up below, indexed by >>>
5. Call the function by typing: have_digits("hello 2x") on the command line.
6. Hit enter to run

The output should display "1", since there is 1 digit in "hello 2x". If it does not, check you entered the inputs 
correctly.

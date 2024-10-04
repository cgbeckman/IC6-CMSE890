# Tutorials

This page gives a tutorial for how to check what action needs to be taken by a thermostat to achieve a desired temperature. Below are two tutorials, one
using a python interface, the other using command line. Both tutorials will operate using 65 F as the current room temperature, and 71 F as the desired room temperature.

# Tutorial for using a python interface.
1.  Open VSCode, Conda, or preferred code editor.
2.  Open a blank script.
3.  Import thermostat.py into the script with the line: from thermostat import my_thermo_stat as thermostat
4.  We will call the function for the previously stated temperatures, 65 and 71. Call the function with the line: output=thermostat(65, 71)
5.  Add a line to check the output: print("Output: ", output)
6.  Run the script

The output should read "heat", because 65 is greater tha 5 degrees below 71. If it does not, check the input was entered in the correct order. If misordered (71, 65), the output will read "AC".

# Tutorial for command line
1. Open command line/terminal
2. Go to the directory where the function thermostat.py is stored.
3. Open python by entering "python" in command line. Hit enter. A new line should show up below, indexed by >>>
4. import the function with: from thermostat import my_thermo_stat
5. Call the function by typing: my_thermo_stat(65, 71) on the command line.
6. Hit enter to run

The output should display "heat". If it does not, check you entered the inputs in the correct order. If misordered, the output will read "AC".



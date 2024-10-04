# Thermostat Explanation

This function changes the status of the thermostat based on temperature and desired temperature.

Args:<ul>
         <li>temp: the current temperature of the room, int</li>
         <li>desired_temp: the desired temperature of the room, int</li>
</ul>
Returns:<ul>
         <li>status: the action that is taken based on the relationship between temp and desired_temp, string</ul>
Authors: <ul>    
<li>Made by Andrew Fullard</li>
 <li>Edited by Cate Beckman for CMSE 890</li>
</ul>

## Code
```def my_thermo_stat(temp : float | int, desired_temp : float | int):
        if temp < desired_temp - 5:
        status = 'Heat'
        elif temp > desired_temp + 5:
             status = 'AC'
        else:
             status = 'off'
        return status```

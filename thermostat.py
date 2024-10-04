def my_thermo_stat(temp : float | int, desired_temp : float | int):
    """
    This function changes the status of the thermostat based on
    temperature and desired temperature. 

    Args:
         temp: the current temperature of the room 
         desired_temp: the desired temperature of the room 
    Returns: 
         status: the action that is taken based on the relationship between temp and desired_temp
    Made by Andrew Fullard 
    Edited by Cate Beckman for CMSE 890
    """
    if temp < desired_temp - 5:
        status = 'Heat'
    elif temp > desired_temp + 5:
        status = 'AC'
    else:
        status = 'off'
    return status


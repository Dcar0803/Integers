import math 

def sqrt_with_check(number):

    if number < 0: 
        raise ValueError("Cannot calculate the square root of a negative number")
    return math.sqrt(number)
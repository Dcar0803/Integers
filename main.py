import math 

def square_root(number):

    """Returns the square root of a number and checks if the number is negative

    Raises:
        ValueError: If the number is negative

    Returns:
        _float: the square root value of a number
    """

    if number < 0: 
        raise ValueError("Cannot calculate the square root of a negative number")
    return math.sqrt(number)
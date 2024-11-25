import math 
import random

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

def random_int(num):

    """ Processes the input number based on specific rules and returns the modified value.

    Raises:
        ValueError: if the number is greater than 4

    Returns:
        float: The processed number after applying the rules.
    """

    num = num or random.randint(1,100)

    if num > 4: 
        raise ValueError("Number shouldn't be greater than 4")
    
    if num % 2 == 1:
        num *=2
    if num % 3 == 0: 
        num /= 3
    if num % 4 == 0:
        num *= 4

    return num

def divisible_by_input(n):
    if n == 0:
        raise ValueError("Division by zero is not allowed.")
    return [i for i in range(1, 11) if i % n == 0]
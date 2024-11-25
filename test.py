import random
from main import square_root

def test_sqrt_with_check():
    assert square_root(4) == 2.0, "Square root of 4 should be 2.0"
    assert square_root(9) == 3.0, "Square root of 9 should be 3.0"
    try:
        square_root(-1)
    except ValueError:
        pass  # Expected exception
    else:
        assert False, "Expected ValueError for negative input"


def test_random_integer():

    for i in range(10):
        num = random.randint(1,100)
        
        if num > 4:
           try:
               random_int(num)
               pass
           except:
               assert False, "Expected ValueError for number > 4"
        
        else:
            result = random_int(num)
            if num % 2 == 1:
                assert result == num * 2, "Odd numbers should be doubled"
            if num % 3 == 0:
                assert result == num // 3, "Numbers divisible by 3 should be divided by 3"
            if num % 4 == 0:
                assert result == num * 4, "Numbers divisible by 4 should be quadrupled"
import random
from main import square_root, random_int, divisible_by_input

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
    for _ in range(10):
        num = random.randint(1, 100)
        
        # Numbers greater than 4 should raise a ValueError
        if num > 4:
            try:
                random_int(num)
                assert False, "Expected ValueError for number > 4"
            except ValueError:
                pass  # Expected behavior
        
        # Numbers 4 or less should follow the rules
        else:
            result = random_int(num)
            
            # Check for odd numbers
            if num % 2 == 1:
                assert result == num * 2, f"Odd number {num} should be doubled"
            
            # Check for numbers divisible by 3
            elif num % 3 == 0:
                assert result == num // 3, f"Number {num} divisible by 3 should be divided by 3"
            
            # Check for numbers divisible by 4
            elif num % 4 == 0:
                assert result == num * 4, f"Number {num} divisible by 4 should be quadrupled"
            
            # Check for even numbers not divisible by 3 or 4
            elif num % 2 == 0 and num % 3 != 0 and num % 4 != 0:
                assert result == num, f"Even number {num} not divisible by 3 or 4 should remain unchanged"

            # Overlapping rules are handled by the first matching condition above

def test_divisible_by_input():
    assert divisible_by_input(2) == [2, 4, 6, 8, 10], "Failed divisible by 2"
    assert divisible_by_input(3) == [3, 6, 9], "Failed divisible by 3"
    assert divisible_by_input(1) == list(range(1, 11)), "Failed divisible by 1"
    try:
        divisible_by_input(0)
    except ValueError:
        pass  # Expected exception
    else:
        assert False, "Expected ValueError for zero input"
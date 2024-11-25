import random
from main import square_root

def test_sqrt_with_check():
    assert sqrt_with_check(4) == 2.0, "Square root of 4 should be 2.0"
    assert sqrt_with_check(9) == 3.0, "Square root of 9 should be 3.0"
    try:
        sqrt_with_check(-1)
    except ValueError:
        pass  # Expected exception
    else:
        assert False, "Expected ValueError for negative input"
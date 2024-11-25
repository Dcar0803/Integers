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
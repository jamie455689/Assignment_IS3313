import my_math

def test_mymath_add():
    assert my_math.add_three(1,2, 3) == 6

def test_mymath_sub():
    assert my_math.subtract_three(8, 2, 1) == 5

def test_mymath_multiply():
    assert my_math.multiply_three(8, 2, 1) == 16

def test_mymath_divide():
    assert my_math.divide_three(8, 2, 1) == 4

def test_mymath_square():
    assert my_math.square(9) == 81

def test_mymath_cube():
    assert my_math.cube(5) == 125
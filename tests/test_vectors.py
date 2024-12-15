from advent_helper.vectors import Vector


def test_vector_addition():
    test_cases = [
        (Vector([1, 2]), Vector([3, 4]), Vector([4, 6])),
        (Vector([1, 2, 3]), Vector([4, 5, 6]), Vector([5, 7, 9])),
        (Vector((4.64, 2.19)), Vector((3.45, 1.23)), Vector((8.09, 3.42))),
    ]

    for left, right, expected in test_cases:
        result = left + right
        assert result == expected
        assert isinstance(result, Vector)

def test_vector_subtraction():
    test_cases = [
        (Vector([1, 2]), Vector([3, 4]), Vector([-2, -2])),
        (Vector([1, 2, 3]), Vector([4, 5, 6]), Vector([-3, -3, -3])),
        (Vector((1.34, 0.3, -23.4)), Vector((0.3, 0.3, 0.3)), Vector((1.04, 0.0, -23.7))),
    ]

    for left, right, expected in test_cases:
        result = left - right
        assert result == expected
        assert isinstance(result, Vector)

def test_vector_multiplication():
    test_cases = [
        (Vector([1, 2]), 3, Vector([3, 6])),
        (Vector([1, 2, 3]), 4, Vector([4, 8, 12])),
    ]

    for left, right, expected in test_cases:
        result = left * right
        assert result == expected
        assert isinstance(result, Vector)

def test_vector_getitem():
    test_cases = [
        (Vector([1, 2]), 1, 2),
        (Vector([1, 2, 3]), 2, 3),
    ]

    for vector, index, expected in test_cases:
        result = vector[index]
        assert result == expected
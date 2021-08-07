from vector import Vector 

def test_equality():
    print("Test equality")
    v1 = Vector([2, 4, 5])
    v2 = Vector([2, 4, 5])
    print(v1 == v2)
    print()

def test_inequality():
    print("Test inequality")
    v1 = Vector([2, 3, 5])
    v2 = Vector([2, 4, 5])
    print(v1 != v2)
    print()

def test_add():
    print("Test add")
    v1 = Vector([2, 3, 5])
    v2 = Vector([2, 4, 5])
    print(v1 + v2)
    print()

def test_mul():
    print("Test add")
    v1 = Vector([2, 3, 5])
    v2 = Vector([2, 4, 5])
    print(v1 * v2)
    print()

test_equality()
test_inequality()
test_add()
test_mul()
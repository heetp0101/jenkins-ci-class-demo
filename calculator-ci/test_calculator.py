# from calculator import add, subtract, multiply

# def test_add():
#     assert add(10, 5) == 15

# def test_subtract():
#     assert subtract(10, 5) == 5

# def test_multiply():
#     assert multiply(10, 5) == 50



from calculator import add, subtract

print("Running tests...")

if add(10, 5) == 15:
    print("Test 1 PASSED")
else:
    print("Test 1 FAILED")
    exit(1)

if subtract(10, 5) == 5:
    print("Test 2 PASSED")
else:
    print("Test 2 FAILED")
    exit(1)

print("All tests PASSED")
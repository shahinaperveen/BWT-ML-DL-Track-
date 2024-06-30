import addition, subtraction, multiplication, division, modulus, advanced # Import specific functions

try:
    # Basic arithmetic operations
    result_add = addition.add(5, 3)
except Exception as e:
    result_add = None
    print(f"Error in addition: {e}")

try:
    result_sub = subtraction.subtract(10, 2)
except Exception as e:
    result_sub = None
    print(f"Error in subtraction: {e}")

try:
    result_mul = multiplication.mul(2, 6)
except Exception as e:
    result_mul = None
    print(f"Error in multiplication: {e}")

try:
    result_div = division.divide(4, 8)
except Exception as e:
    result_div = None
    print(f"Error in division: {e}")

try:
    result_rem = modulus.remainder(4, 6)
except Exception as e:
    result_rem = None
    print(f"Error in modulus operation: {e}")

print(f"Addition: {result_add}, Subtraction: {result_sub}, multiplication: {result_mul}, division: {result_div}, remainder: {result_rem}")

try:
    # Advanced operations
    result_pow = advanced.power(2, 4)
except Exception as e:
    result_pow = None
    print(f"Error in power calculation: {e}")

try:
    result_sqrt = advanced.sqrt(16)
except Exception as e:
    result_sqrt = None
    print(f"Error in square root calculation: {e}")

print(f"Power: {result_pow}, Square Root: {result_sqrt}")

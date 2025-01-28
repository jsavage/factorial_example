import pytest
from hypothesis import given, strategies as st
from factorial import factorial

# Original tests
def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(3) == 6

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-5)

# Large number testing
def test_factorial_large_numbers():
    assert factorial(10) == 3628800
    assert factorial(20) == 2432902008176640000

# Property-based testing
@given(st.integers(min_value=0, max_value=20))
def test_factorial_properties(n):
    result = factorial(n)
    if n > 0:
        assert result == n * factorial(n-1)
    else:
        assert result == 1

# Boundary testing
def test_factorial_boundary():
    assert factorial(1) == 1
    with pytest.raises(ValueError):
        factorial(1000)  # Test upper limit

# Type checking
def test_factorial_type_validation():
    with pytest.raises(TypeError):
        factorial(3.14)
    with pytest.raises(TypeError):
        factorial("5")

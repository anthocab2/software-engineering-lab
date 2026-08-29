"""
Practice: Local and global variable scope.

This exercise demonstrates that variables created inside a function
have a local scope. A local variable can have the same name as a
global variable without replacing the global value.
"""

price = 100


def calculate():
    """Calculate a value using a local price variable."""
    price = 50
    total = price * 2

    return total


result = calculate()

# result contains the value returned by calculate().
print(f"Function result: {result}")

# This price refers to the global variable, not the local one.
print(f"Global price: {price}")

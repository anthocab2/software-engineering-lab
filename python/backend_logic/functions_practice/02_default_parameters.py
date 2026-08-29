"""
Practice: Default parameters and keyword arguments.

This exercise demonstrates how a function can have an optional
parameter with a default value. It also shows how keyword arguments
allow values to be passed by parameter name instead of position.
"""


def calculate_price(price, quantity, discount=0):
    """Calculate the total price after applying an optional discount."""
    return price * quantity - discount


# discount uses its default value of 0.
price_without_discount = calculate_price(100, 2)

# Arguments are explicitly assigned by name.
price_with_discount = calculate_price(
    price=100,
    quantity=2,
    discount=50,
)

# Keyword arguments can be written in a different order.
another_price = calculate_price(
    discount=20,
    quantity=3,
    price=50,
)

print(price_without_discount)
print(price_with_discount)
print(another_price)

"""
Practice: Parameters, arguments, dictionaries, and return.

This exercise shows how a function can receive a complete dictionary
as an argument, access its values, perform a calculation, and return
the result to another part of the program.
"""

product = {
    "name": "Laptop",
    "price": 800,
    "quantity": 2,
}


def calculate_product_value(product):
    """Return the total inventory value of one product."""
    return product["price"] * product["quantity"]


# The value returned by the function is stored in result.
result = calculate_product_value(product)

print(f'Product: {product["name"]}')
print(f"Inventory value: {result}")

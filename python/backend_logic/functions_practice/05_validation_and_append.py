"""
Practice: Validation, loops, conditions, and list append.

This exercise validates multiple products using a reusable function.

The program:
1. Iterates through a list of product dictionaries.
2. Validates each product.
3. Checks the value returned by the validation function.
4. Uses append() to store only valid products in a new list.

This is similar to filtering incoming data in a backend application.
"""

products = [
    {"name": "Laptop", "price": 800, "quantity": 2},
    {"name": "", "price": 50, "quantity": 3},
    {"name": "Mouse", "price": 0, "quantity": 5},
    {"name": "Monitor", "price": 200, "quantity": 4},
]


def validate_product(product):
    """Validate one product and return its validation status."""
    if product["name"] == "":
        return "Name required"

    if product["price"] <= 0:
        return "Invalid price"

    if product["quantity"] < 0:
        return "Invalid quantity"

    return "Valid product"


valid_products = []

for product in products:
    result = validate_product(product)

    # Only valid products are added to the new list.
    if result == "Valid product":
        valid_products.append(product)


print(valid_products)

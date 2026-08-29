"""
Practice: Validation and early return.

This exercise demonstrates how a function can validate data one rule
at a time. When a validation fails, return immediately stops the
function and sends an error message back to the caller.

This pattern is useful in backend applications when validating data
before processing it.
"""


def validate_order(order):
    """Validate an order and return its validation status."""
    if order["id"] <= 0:
        return "Invalid ID"

    if order["total"] <= 0:
        return "Invalid total"

    if order["paid"] == False:
        return "Order not paid"

    return "Valid order"


order_1 = {
    "id": 101,
    "total": 250,
    "paid": True,
}

order_2 = {
    "id": 102,
    "total": 100,
    "paid": False,
}


print(validate_order(order_1))
print(validate_order(order_2))

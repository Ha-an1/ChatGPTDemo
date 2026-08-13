def calculate(operation, a, b):
    """Perform a basic arithmetic operation."""
    operations = {
        "add": lambda: a + b,
        "subtract": lambda: a - b,
        "multiply": lambda: a * b,
        "divide": lambda: a / b,
    }

    if operation not in operations:
        raise ValueError("Unsupported operation")

    if operation == "divide" and b == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return operations[operation]()

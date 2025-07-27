def perform_operation(num1, num2, operation):
    """
    A function that returns a result based on given operation add, divide, subtract
    , or multiply
    """

    if operation=='add':
        return num1 + num2
    elif operation=='subtract':
        return num1 - num2
    elif operation=='multiply':
        return num1 * num2
    elif operation=='divide':
        if num2 == 0:
            return "Cannot divide by zero."
        else:
            return num1 / num2
    else:
        return "Invalid Operation, Enter a Valid Operation"

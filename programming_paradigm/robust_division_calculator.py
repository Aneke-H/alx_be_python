def safe_divide(numerator, denominator):
    """Safely divides two numbers, returning 0 if the denominator is zero."""
    try:
        numerator=float(numerator)
        denominator=float(denominator)
        result= numerator / denominator
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    else:
        return f"The result of the division is {result}"

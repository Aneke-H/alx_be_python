class Calculator:
    calculation_type = "Arithmetic Operations"
    """A simple calculator class to demonstrate static methods."""
    @staticmethod
    def add(a, b):
        """Return the sum of x and y."""
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """Return the product of x and y."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
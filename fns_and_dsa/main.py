from arithmetic_operations import perform_operation
# from test_arithmetic_operations import  test

def main():
    """The Entry point to the program"""
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

    # test()

if __name__ == "__main__":
    main()

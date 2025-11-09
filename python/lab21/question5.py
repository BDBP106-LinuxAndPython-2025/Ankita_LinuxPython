
def calculate(n1, n2, operation):
    try:
        if operation == "add":
            result = n1 + n2
        elif operation == "subtract":
            result = n1 - n2
        elif operation == "multiply":
            result = n1 * n2
        elif operation == "divide":
            result = n1 / n2
        else:
            # raising an error if operator is not valid
            raise ValueError("Invalid operation! Use add, subtract, multiply, or divide.")
        print(f"Result of {operation} is:", result)

    except ValueError as ve:
        print("Error:", ve)

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    finally:
        print("Operation completed.\n")

# 1. Valid addition
calculate(10, 5, "add")

# 2. Valid multiplication
calculate(4, 3, "multiply")

# 3. Division by zero (ZeroDivisionError)
calculate(10, 0, "divide")

# 4. Invalid operation (ValueError)
calculate(7, 2, "modulus")

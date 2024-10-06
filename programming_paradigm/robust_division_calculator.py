def safe_divide(numerator, denominator):
    numerator = int(input("Enter your numerator"))
    denominator = int(input("Enter your denominator"))
    try:
        output = numerator / denominator
        return f"The result of the division is {output}"
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero.")
    except ValueError as e:
        print("Please enter numeric values only.")
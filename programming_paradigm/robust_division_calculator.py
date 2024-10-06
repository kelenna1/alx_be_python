def safe_divide(numerator, denominator):
    
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        output = numerator / denominator
        return f"The result of the division is {output}"
    except ZeroDivisionError as e:
        return "Error: Cannot divide by zero."
    except ValueError as e:
        return "Error: Please enter numeric values only."


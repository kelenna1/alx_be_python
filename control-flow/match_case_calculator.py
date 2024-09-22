def main():
    try:
        num_1 = int(input("Enter the first number: "))
        num_2 = int(input("Enter the second number: "))
    except ValueError:
        print("invalid input, enter a numeric value")
        return
    operation = input("Choose the operation (+, -, *, /): ")

    match operation:
        case "+":
            result = num_1 + num_2
        case "-":
            result = num_1 - num_2
        case "*":
            result = num_1 * num_2
        case "/":
            if num_2 == 0:
                print("Cannot divided by zero")
                return
            else:
                result = num_1 / num_2
        case _:
            print("Invalid operation. Please choose +, -, *, or /.")
            return
    print(f"The result is {result}.")

main()



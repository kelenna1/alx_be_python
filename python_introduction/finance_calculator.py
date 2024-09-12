income = int(input("Enter your monthly income:"))
expenses = int(input("Enter your total monthly expenses:"))
 
savings = income - expenses
annual_savings = savings * 12 + (savings * 12 * 0.05)
if expenses >= income:
    print("You made no savings this month")
else:
    print(f"Your monthly savings are ${savings}.")
    print(f"Projected savings after one year, with interest, is: ${annual_savings}")

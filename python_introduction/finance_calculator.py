monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - total_monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 0.05 * 12)
print (f"your monthly savings are ${monthly_savings}.")
print (f"Your projected savings after one year, with interest, is: ${int(projected_savings)}.")
monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - total_monthly_expenses
annual_savings = monthly_savings * 12
annual_compound_interest = monthly_savings * 0.05 * 12
projected_yearly_savings = annual_savings + annual_compound_interest
print (f"your monthly savings are ${monthly_savings}.")
print (f"Your projected savings after one year, with interest, is: ${int(projected_yearly_savings)}.")
monthly_income = int(input("Enter your monthly income: "))
Total_monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - Total_monthly_expenses
yearly_savings = int((monthly_savings * 12) + (monthly_savings * 0.05 * 12))
print (f"your monthly savings are ${monthly_savings}.")
print (f"Your projected savings after one year, with interest, is: ${yearly_savings}.")
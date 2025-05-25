monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - total_monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Monthly Savings: ${monthly_savings}")
print(f"Projected Annual Savings: ${int(projected_savings)}.")

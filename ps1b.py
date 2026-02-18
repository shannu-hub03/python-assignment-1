# Q = 2
annual_salary = float(input("Enter the annual salary: "))
portion_saved = float(input("Enter the portion save: "))
total_cost = float(input("Enter the cost of dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise: "))
portion_down_payment = 0.25
annual_return = 0.04
down_payment = total_cost * portion_down_payment
current_savings = 0
monthly_salary = annual_salary / 12
months = 0
while current_savings < down_payment:
    current_savings += current_savings * annual_return / 12
    current_savings += monthly_salary * portion_saved
    months += 1
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12
print(f"Number of months: {months}")

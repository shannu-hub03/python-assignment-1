# Q = 3
starting_salary = float(input("Enter the starting salary: "))

total_cost = 1000000
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
annual_return = 0.04
semi_annual_raise = 0.07
months = 36

low = 0
high = 10000
steps = 0

current_savings = 0
annual_salary = starting_salary
monthly_salary = annual_salary / 12

for month in range(1, months+1):
    current_savings += current_savings * annual_return / 12
    current_savings += monthly_salary * 1.0
    if month % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12

if current_savings < down_payment:
    print("It is not possible to pay the down payment in three years.")
else:

    while True:

        mid = (low + high) // 2
        portion_saved = mid / 10000.0

        current_savings = 0
        annual_salary = starting_salary
        monthly_salary = annual_salary / 12

        for month in range(1, months+1):

            current_savings += current_savings * annual_return / 12
            current_savings += monthly_salary * portion_saved

            if month % 6 == 0:
                annual_salary += annual_salary * semi_annual_raise
                monthly_salary = annual_salary / 12

        steps += 1

        if abs(current_savings - down_payment) <= 100:
            print("Best savings rate:", round(portion_saved, 4))
            print("Steps in bisection search:", steps)
            break

        elif current_savings < down_payment:
            low = mid

        else:
            high = mid
"""
(Financial application: payroll) Write a program that reads the following information
and prints a payroll statement:
Employee’s name (e.g., Smith)
Number of hours worked in a week (e.g., 10)
Hourly pay rate (e.g., 9.75)
Federal tax withholding rate (e.g., 20%)
State tax withholding rate (e.g., 9%)
"""
name = input("Employee’s name: ")
hours = eval(input("Number of hours worked in a week: "))
hourly_payrate = eval(input("Hourly pay rate: "))
federal_tax = eval(input("Federal tax withholding rate: "))
state_tax = eval(input("State tax withholding rate: "))

total_pay = hourly_payrate * hours
federal_pay = total_pay * federal_tax
state_pay = total_pay * state_tax
print()
print()
print("Employee Name: ", name)
print("hours worked: ", hours)
print("Pay Rate: $" + str(hourly_payrate))
print("Gross Rate: $" + str(total_pay))

print("Deductions: ")
print('Federal withholding: (' + str(federal_tax * 100) + '%): $' + str(federal_pay))
print('State withholding:  (' + str(state_tax * 100) + '%): $' + str(state_pay))
print('Total Deduction: '+str(federal_pay+state_pay))
print('Net Pay: $'+str(total_pay - (federal_pay+state_pay)))

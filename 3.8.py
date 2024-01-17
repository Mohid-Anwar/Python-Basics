"""
(Financial application: monetary units) Rewrite Listing 3.4, ComputeChange.py,
to fix the possible loss of accuracy when converting a float value to an int value.
Enter the input as an integer whose last two digits represent the cents. For example,
the input 1156 represents 11 dollars and 56 cents.
"""
amount_in_points = eval(input("Enter amount of cash eg.1185: "))

remaining = amount_in_points  # 2201

dollars = remaining // 100
cents = remaining % 100

print("Your amount ", remaining, 'consists of')
print("No. of dollars: $", dollars)
print("No. of cents: ", cents,'cents')

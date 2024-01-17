income = 45000
taxPayable = 0

if income <= 10000:
    taxPayable = 0
elif income <= 20000:
    taxPayable = (income - 10000) * 10 / 100
else:
    taxPayable = 0

    taxPayable = 10000 * 10 / 100

    taxPayable += (income - 20000) * 20 / 100

print("Total tax to pay is", taxPayable)
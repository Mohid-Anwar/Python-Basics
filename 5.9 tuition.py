current_year = 0
tuition_value = 10000
total_value = 0
percentage_increase = 5 / 100

while current_year < 10:
    tuition_value += ((5 / 100) * tuition_value)

    current_year += 1
x = round(tuition_value)
print("after 10 years tuition is", (str(x)))

for current_year in range(10, 14):
    tuition_value += ((5 / 100) * tuition_value)
    current_year += 1
    total_value += tuition_value
y = round(total_value)
print("Tuition 4 yrs frm now is", str(y))

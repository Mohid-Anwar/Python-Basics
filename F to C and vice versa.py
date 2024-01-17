# converts C to F and F to C

temp = input("enter the temp eg 42F or 42C:  ")
degree = temp[:-1]
print(degree)
convention = temp[-1]
result = ''
new_convention = ''
if convention == "F":
    # Acha == for check hota hai. To assign a value use = only
    new_convention = 'C'
    result = int(round((eval(degree) - 32) * 5 / 9))
elif convention == "C":
    result = int(round((9 * eval(degree)) / 5 + 32))
    new_convention = "F"
else:
    print("input proper convention")

# line 19 main space ni deni wrna else main aa jaye ga anddd degree ki jagah result likhna hai
print(f"the temperature is {result}{new_convention}")

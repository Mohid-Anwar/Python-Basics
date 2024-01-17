start_value = 1
last_value = 0
while last_value < 10:
    if start_value % 2 == 0:
        print(start_value)
        last_value = last_value + 1
        start_value = start_value + 1
    else:
        start_value = start_value + 1
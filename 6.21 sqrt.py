def sqrt(num):
    last_guess = 1
    next_guess = (last_guess + (num / last_guess)) / 2
    while abs(last_guess - next_guess) > 0.0001:
        last_guess = next_guess
        next_guess = (last_guess + (num / last_guess)) / 2
    return next_guess


number = eval(input("Welcome. Enter num: "))
print(sqrt(number))

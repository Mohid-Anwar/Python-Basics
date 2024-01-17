password = input("Hello Please decide on a password")
le = len(password)
if ('@' in password) and le >= 8:
    print("Accepted")
else:
    if le == 0:
        print("You have written nothing")
    else:
        print("Your password is small and/or does not contain special char @")

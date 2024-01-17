password = input("Hello Please decide on a password ")
le = len(password)
if '@' in password:
    if le >= 8:
        print("Accepted")
elif le == 0:
    print("You have written nothing")
else:
    print("Your password is small and does not contain special char @")

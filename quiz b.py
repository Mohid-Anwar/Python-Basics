def isPalindrome(x):
    if len(x) < 2:
        return True


    if (x[0].lower() == x[-1].lower()) and isPalindrome(x[1: -1]):
        print("Palindrome")
    else:
        print("Not Palindrome")

a = "121"
isPalindrome(a)
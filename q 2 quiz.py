def isPalindrome (x) :

    if len(x) < 2:
        return True

    # recursive cases
    # if first or last are not letters, remove that character and check again
    if not x[0] . isalpha( ) :
        return isPalindrome(x[1: ])
    if not x[- 1] . isalpha() :

        return isPalindrome(x[ : -1])

    if (x[0] . lower() == x[-1]. lower() ) and isPalindrome(stri[1: -1]) :
         print("Palindrome")
    else:
        print("Not Palindrome")



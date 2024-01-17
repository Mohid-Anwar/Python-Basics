"""Write a program for a cash counter that input a payable amount from customer (less than 10000)

and calculate remaining amount.

This program passes remaining amount to a function that calculates how many 1000, 500, 100, 50, 20, 10 currency notes have to return back to the
customer."""

userInput = int(input("Payable Amount: "))
while userInput > 10000:
    userInput = int(input("Value less than 10k: "))
print("Return The following Notes")
thousands = userInput // 1000
userInput = userInput - (1000*thousands)
print("1000s", thousands)

five_hundreds = userInput // 500
userInput = userInput - (500*five_hundreds)
print("500:", five_hundreds)

hundreds = userInput // 100
print("100s:", hundreds)

userInput = userInput - (100* hundreds)
fifty = userInput // 50
print("50s:", fifty)

userInput = userInput - (50*fifty)
twenties = userInput // 20
print("20s:", twenties)

userInput = userInput - (20*twenties)
ones = userInput // 1
userInput = userInput - (1*ones)
print("1s:", ones)


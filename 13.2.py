metal = input("gold, silver or diamond ")
metal = metal.lower()
if metal == 'gold':
    print('Price of gold is 8916 per gram ')
else:
    if metal == 'silver':
        print('Price of silver is 124 per gram ')
    else:
        if metal == 'diamond':
            print('Price of diamond is 658466 per gram ')
        else:
            print('Invalid entry')

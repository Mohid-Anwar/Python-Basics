city = (input('''Enter one of the countries to get its capital 
                Pakistan
                India
                UK
'''))
city = city.lower()
if city == 'pakistan':
    print("Islamabad")
else:
    if city == 'india':
        print('New Delhi')
    else:
        if city == 'uk':
            print('London')
        else:
            print("Invalid country entered")

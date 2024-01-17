city = (input('''Enter one of the countries to get its capital 
                Pakistan
                India
                UK
'''))
city = city.lower()
if city == 'pakistan':
    print("Islamabad")
elif city == 'india':
    print('New Delhi')
elif city == 'uk':
    print('London')
else:
    print("Invalid country entered")

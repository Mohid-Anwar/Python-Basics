license = input('Do you have license Y or N : ')
id = ''
license = license.upper()

if license == 'Y' and license != 'N':
    print('Challan on license')
elif license == 'N' and license != 'Y':
    id = input('do you have id Y or N : ')
    id= id.upper()
    if id == 'Y':
        print('Challan on id')
    else:
        print('Taken to jail')

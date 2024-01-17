items = eval(input('How many items: '))
coupon = input('Coupon Y or N : ')
coupon = coupon.upper()
if items > 10:
    if coupon == 'Y':
        print('10% discount due to coupon')
    else:
        print('No discount')
else:
    if items < 10:
        print('10% discount because of less items ')
        if coupon == 'Y':
            print('10% more discount because of coupon')
    else:
        print('No discount')

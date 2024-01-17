items = eval(input('How many items: '))
coupon = input('Coupon Y or N : ')
coupon = coupon.upper()
if items < 10 and coupon == 'Y':
    print('10% discount because of less items ')
    print('10% discount due to coupon')
elif items > 10 and coupon == 'N':
    print('No discount')
elif items < 10 and coupon == 'N':
    print('10% discount because of less items ')
elif items > 10 and coupon == 'Y':
    print('10% discount due to coupon')

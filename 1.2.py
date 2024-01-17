num = eval(input("Enter Marks scored : "))
if num >= 90:
    print('A')
else:
    if num >= 80:
        print('B')
    else:
        if num >= 70:
            print('C')
        else:
            if num >= 60:
                print('D')
            else:
                if num >= 50:
                    print('B')
                else:
                    print('Fail')

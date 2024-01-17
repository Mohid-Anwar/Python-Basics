def PrimeNumberFunction():
    limit_prime_number = 10000

    current_number_being_checked = 2

    while current_number_being_checked < limit_prime_number:
        prime_check = True
        divided_by = 2
        while divided_by <= current_number_being_checked / 2:
            if current_number_being_checked % divided_by == 0:
                prime_check = False
            divided_by += 1
        if prime_check:
            print(current_number_being_checked, end=" ")
        current_number_being_checked += 1


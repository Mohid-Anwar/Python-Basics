user_input = int(input("Enter value: "))
descending = user_input
chain_length = 0
priv_diff = 0

while True:
    descending = list(str(descending))
    descending.sort()

    ascending = descending
    ascending = int("".join(ascending))

    descending.reverse()
    descending = "".join(descending)
    descending = int(descending)

    diff = descending - ascending
    chain_length += 1

    descending = diff
    if priv_diff == diff:
        break

    priv_diff = diff
print(f"Original num {user_input} and chain length = {chain_length} ")

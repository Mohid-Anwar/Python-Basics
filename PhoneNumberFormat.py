dict_alphabets = {'-': '-', "a": "1", "b": "2", "c": "3",
                  'd': '3', 'e': '3', 'f': '3',
                  'g': '4', 'h': '4', 'i': '4',
                  'j': '5', 'k': '5', 'l': '5',
                  'm': '6', 'n': '6', 'o': '6',
                  'p': '7', 'q': '7', 'r': '7', 's': '7',
                  't': '8', 'u': '8', 'v': '8',
                  'w': '9', 'x': '9', 'y': '9', 'z': '9'}

usr_Input_phone_no = input('XXX-XXX-XXXX is format. Enter your Phone number ').lower()
len_check_phone_no = usr_Input_phone_no.split("-")

while len(len_check_phone_no[1]) != 3 or len(len_check_phone_no[0]) != 3 or len(len_check_phone_no[2]) != 4:
    usr_Input_phone_no = input('XXX-XXX-XXXX is the correct Format. This is incorrect format. Re-enter: ').lower()
    len_check_phone_no = usr_Input_phone_no.split("-")

print("The Phone Number is : ", end="")
print(usr_Input_phone_no[:3], end="")
for letter in usr_Input_phone_no[3:]:
    print(dict_alphabets[letter], end="")

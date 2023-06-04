def password_check(passed_word):
    counter = 0
    if len(passed_word) not in range(6, 11):
        print("Password must be between 6 and 10 characters")
    for letter in passed_word:
        check = letter
        if ord(check) in range(48, 58) or ord(check) in range(65, 91) or ord(check) in range(97, 123):
            continue
        else:
            print("Password must consist only of letters and digits")
            break
    for letter in passed_word:
        if ord(letter) in (range(48, 58)):
            counter += 1
    if counter < 2:
        print("Password must have at least 2 digits")
    else:
        return print("Password is valid")


password = input()
password_check(password)

def correctpassword(password):
    correct_len = False
    has_upper = False
    has_lower = False
    has_digit = False

    if len(password) >= 7:
        correct_len = True

    for each in password:
        if each.isupper():
            has_upper = True
        if each.islower():
            has_lower = True
        if each.isdigit():
            has_digit = True

    if correct_len and has_upper and has_lower and has_digit:
        isvalid = True
    else:
        isvalid = False
        return isvalid

def main():
    password = input("Enter your password: ")
    while correctpassword(password):
        print("The password is valid")
    else:
        print("The password is not valid")
        password = input("Enter your password: ")


main()
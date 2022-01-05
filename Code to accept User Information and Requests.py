# Code 1
def main():
    print("WELCOME")
    get_request()
    print("GOODBYE")

def get_request():
    request = input("Enter your request:")
    print(request)
    print("is that your last request?")

main()


# Code 2
name = input("Enter your name: ")
address = input("Enter your address: ")

def bio_data(n, a):
    age = int(input("Enter your age: "))
    print("Your name is",n)
    print("Your address is ",a)
    print("You are", age,"years old")

bio_data(address, name)

# Code 3
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

# Code 4
username = ['Grimlock', 'Jago', 'Roman', 'Eight', 'Phantom']
password = ['123', '234', '345', '456', '567']
print(username),
print("\n")

nameenter = input("Enter your username: ")
passenter = input("Enter the Password: ")

if nameenter in username and passenter in password:
    print("Access Granted ˆ_ˆ")
else:
    print("Access Denied")
    print("\n")
    newusername = input("Enter a new username: ")
    newpass = input("Enter a new password: ")
    username.append(newusername)
    password.append(newpass)
    print("Login details have been saved and Access is Granted ˆ_ˆ")
    print("This is proof: ")
    print(username)
    print(password)
    print("\n")

nameposition = username.index(input("Enter the username you are looking for: "))
print("The username you are looking for is in position:", nameposition)
print("\n")

input("To change your username press enter")
oldusername = input("Enter your username please: ")
if oldusername in username:
    print("User Exists ˆ_ˆ")
    new2user = input("Enter the new username you want to use: ")
    pos = int(input("Enter the position you want the new username to go to: "))
    username.insert(pos, new2user)
else:
    print("Omo jazz up")

if new2user in username:
    print("Change successful!")
    print(username)

print("\n")
print("This is the sorted list BISHHH")
username.sort()
print(username)

rem = input("Press enter if you want to remove a username, but boss abeg no do am: ")
username.remove(rem)

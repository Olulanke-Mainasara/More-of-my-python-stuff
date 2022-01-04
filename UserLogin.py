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
    print("Change successful!,Opooooorr!!!")
    print(username)

print("\n")
print("This is the sorted list BISHHH")
username.sort()
print(username)

rem = input("Press enter if you want to remove a username, but boss abeg no do am: ")
username.remove(rem)

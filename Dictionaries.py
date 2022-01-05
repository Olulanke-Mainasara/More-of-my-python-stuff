# Code 1
def main():
    mydict = {}
    userinput = int(input("Enter the length of your dictionary: "))
    for key in range(userinput):
        print(key)
        value = input("The word form of the number displayed: ")
        mydict[key]=value
        print(mydict)
    print("\n")
    print("This is post formatting of the phonebook: ")
    mydict.clear()
    print(mydict)


main()

# Code 2
def main():
    inventory = {"Noreos":20, "Bread":10, "Biscuit":50, "Candy":100, "Food":20}
    print(inventory.keys())
    acquire = input("Which product do you want to buy: ")
    amount = int(input("What quantity of this product do you want: "))
    if acquire not in inventory:
        print("Sorry, we don't have this product.")
    elif inventory[acquire] == 0:
        print("Sorry, we are out of stock but please do come bck to check again later.")
    elif amount > inventory[acquire]:
        print("Sorry, we don't have enough for your purchase.")
    else:
        inventory[acquire] = inventory[acquire] = amount
        print("Good choice.")

    print(inventory)
    remove = input("Which item do you want to remove: ")
    print(inventory.pop(remove))
    print(inventory)


main()

#Code 3
def main():
    phonedict = {"Grimlock":"08181120601", "Roman":"08023456578", "Phantom":"090245457687", "Eight":"0704523213454"}
    phonename = input("Enter the new name to be saved: ")
    phoneno = input("Enter the new phone number: ")
    phonedict[phonename]=phoneno
    print(phonedict)

    print("\n")
    lookedno = input("Enter the number you want to look for: ")
    print(phonedict.get(lookedno))

    print("\n")
    print("After deleting the specified number, this is the updated phonebook")
    del phonedict["Grimlock"]
    print(phonedict)



main()

# Code 4
def main():
    mydict = {1:"January",2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
    userinput = input("Enter the date in this format DD/MM/YYYY: ")
    usercomp = userinput.split("/")
    print(usercomp)
    print(mydict[int(usercomp[1])], (usercomp[0]), ",",  (usercomp[2]), ".")


main()

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

'''
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



myset = set(["one", "two", "three"])
myset.add(7)
myset.update([3,2,4])

print(myset)


set1 = set([1,2,3,4,5])
set2 = set([6,7,8,9,0])
setu = set1.union(set2)
print(setu)
'''


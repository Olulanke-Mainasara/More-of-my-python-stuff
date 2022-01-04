listacq = int(input("Enter the value of the list: "))
listrange = []

for item in range(listacq):
    newval = int(input("Enter a number to be added: "))
    listrange.append(newval)
    print(listrange)


ops = int(input("Which operation do u want to perform: \n1. append the list\n2. insert a number\n3. remove a number\n4. sort the list\n: "))

if (ops == 1):
    newapp = int(input("Enter the new number u want to add"))
    listrange.append(listrange)
    print(listrange)


elif (ops == 2):
    newins = input("Enter the new number you want to insert: ")
    pos = int(input("Enter the position you want the new number to go to: "))
    listrange.insert(pos, listrange)
    print(listrange)

elif (ops == 3):
    numrem = input("Which number do you want to remove: ")
    listrange.remove(numrem)
    print(listrange)

elif (ops == 4):
    listrange.sort()
    print(listrange)

else:
    print("Choose an accurate operation number BOSS!")



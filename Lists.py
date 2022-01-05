# Code 1
mylist = list(range(2, 16))
number = int(input("Enter the guess number: "))
if number in mylist:
    print("You guessed right")
else:
    print("You guessed wrong")

# Code 2
mylist = list(range(3, 10))
count = 0
for I in mylist:
    count += 1
print(count)

# Code 3
mylist = [0,1,3,7,9]
indexval = int(input("index val: "))
sizemylist = len(mylist)
if sizemylist <= indexval:
    print("Try again")
    indexval = int(input("Enter indexval: "))
else:
    print("correct")

# Code 4
listA = list(range(2, 5))
listB = list(range(5, 10))
theOGlist = listA + listB
print(theOGlist)
listD = theOGlist[0 : 3]
listE = theOGlist[3 : 8]
print(listD)
print(listE)


# Code 5
listacq = int(input("Enter the value of the list: "))
listrange = []

for item in range(listacq):
    newval = int(input("Enter a number to be added: "))
    listrange.append(newval)
    print(listrange)


ops = int(input("Which operation do u want to perform: \n1. append the list\n2. insert a number\n3. remove a number\n4. sort the list\n: "))

if (ops == 1):
    newapp = int(input("Enter the new number you want to add"))
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



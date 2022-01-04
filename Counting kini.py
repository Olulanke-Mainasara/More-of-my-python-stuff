

mylist = list(range(3, 10))
count = 0
for I in mylist:
    count += 1
print(count)

mylist = [0,1,3,7,9]
indexval = int(input("index val: "))
sizemylist = len(mylist)
if sizemylist <= indexval:
    print("Try again")
    indexval = int(input("Enter indexval: "))
else:
    print("correct")


listA = list(range(2, 5))
listB = list(range(5, 10))
theOGlist = listA + listB
print(theOGlist)
listD = theOGlist[0 : 3]
listE = theOGlist[3 : 8]
print(listD)
print(listE)

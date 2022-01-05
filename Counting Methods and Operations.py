# Code for Counting the  number of figures between a given range
mylist = list(range(3, 10))
count = 0
for I in mylist:
    count += 1
print(count)

# Code to check if the number entered by the user is greater than the size of the array of numbers giving
mylist = [0,1,3,7,9]
indexval = int(input("index val: "))
sizemylist = len(mylist)
if sizemylist <= indexval:
    print("Try again")
    indexval = int(input("Enter indexval: "))
else:
    print("correct")

# Code to show the concatenation of two lists
listA = list(range(2, 5))
listB = list(range(5, 10))
theOGlist = listA + listB
print(theOGlist)
listD = theOGlist[0 : 3]
listE = theOGlist[3 : 8]
print(listD)
print(listE)

# Basic Arithmetics
def add(a,b):
    sum = a + b
    print(sum)

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second numbers: "))
add(num_1, num_2)

# Code to Edit the Value already given by the Programmer
def main():
    value = 99
    print("The value is",value)
    change_me(value)
    print("Back in main the value is",value)

def change_me(arg):
        print("I am changing the value.")
        arg = 0
        print("Now the value is", arg)

main()
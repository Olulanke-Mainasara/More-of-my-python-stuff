# Code 1
even_numbers = [2,4,6,8,10]
print(even_numbers)
for item in even_numbers:
    print(item)
print(even_numbers[1])

# Code 2
names = ["Roman", "Phantom", "Jago", "Eight", "Grimlock"]
print(names)
for N in names:
    print(N)
print(names[0])

# Code 3
info = ["Alicia", 27, 1550.87]
print(info)
for I in info:
    if I == 27:
        print("Found", I)
    else:
        print("Item not found")

# Code 4
numbers = list(range(5))
print(numbers)
numbers2 = list(range(2, 16))
print(numbers2)

count = int(input("Enter times: "))
mylist = list(range(2, count))
mylistsize = len(mylist)
print(mylistsize)

mylist = list(range(3, 10))
name = input("Enter your name: ")
address = input("Enter your address: ")

def bio_data(n, a):
    age = int(input("Enter your age: "))
    print("Your name is",n)
    print("Your address is ",a)
    print("You are", age,"years old")

bio_data(address, name)
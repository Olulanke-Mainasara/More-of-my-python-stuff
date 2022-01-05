def main():
    print("WELCOME")
    get_request()
    print("GOODBYE")

def get_request():
    request = input("Enter your request:")
    print(request)
    print("is that your last request?")

main()

name = input("Enter your name: ")
address = input("Enter your address: ")

def bio_data(n, a):
    age = int(input("Enter your age: "))
    print("Your name is",n)
    print("Your address is ",a)
    print("You are", age,"years old")

bio_data(address, name)
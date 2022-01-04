def main():
    found = False
    search = input("Enter a description to search for: ")
    new_qty = int(input("Enter the new quantity: "))

    coffe_file = open("coffee.txt", "r")
    temp_file = open("temp.txt", "w")
    descr = coffee
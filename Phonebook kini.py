def main():
    phonedict = {"Grimlock":"08181120601", "Roman":"08023456578", "Phantom":"090245457687", "Eight":"0704523213454"}
    phonename = input("Enter the new name to be saved: ")
    phoneno = input("Enter the new phone number: ")
    phonedict[phonename]=phoneno
    print(phonedict)

    print("\n")
    lookedno = input("Enter the number you want to look for: ")
    print(phonedict.get(lookedno))

    print("\n")
    print("After deleting the specified number, this is the updated phonebook")
    del phonedict["Grimlock"]
    print(phonedict)



main()
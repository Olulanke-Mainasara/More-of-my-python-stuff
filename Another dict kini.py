def main():
    mydict = {}
    userinput = int(input("Enter the length of your dictionary: "))
    for key in range(userinput):
        print(key)
        value = input("The word form of the number displayed: ")
        mydict[key]=value
        print(mydict)
    print("\n")
    print("This is post formatting of the phonebook: ")
    mydict.clear()
    print(mydict)


main()
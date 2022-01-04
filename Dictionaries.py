def main():
    mydict = {1:"January",2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
    userinput = input("Enter the date in this format DD/MM/YYYY: ")
    usercomp = userinput.split("/")
    print(usercomp)
    print(mydict[int(usercomp[1])], (usercomp[0]), ",",  (usercomp[2]), ".")


main()
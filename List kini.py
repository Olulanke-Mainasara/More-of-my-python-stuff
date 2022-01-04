mylist = list(range(2, 16))
number = int(input("Enter the guess number: "))
if number in mylist:
    print("You guessed right")
else:
    print("You guessed wrong")


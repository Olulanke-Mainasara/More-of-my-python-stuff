def main():
    Body()

def Body():
    print("WELCOME")
    addition()
    print("Farewell ˆ_ˆ")

def addition():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    sum = num1 + num2
    print("The sum is ", sum)
    print("Anything else?")

main()
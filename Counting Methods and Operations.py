# Code 1
def add(a,b):
    sum = a + b
    print(sum)

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second numbers: "))
add(num_1, num_2)

# Code 2
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

# Code 3
def main():
    num_1 = int(input("Enter the first number: "))
    num_2 = int(input("Enter the second number: "))
    num_3 = int(input("Enter the third number: "))
    num_4 = int(input("Enter the fourth number: "))
    num_5 = int(input("Enter the fifth number: "))
    res1, res2 = compute(num_1, num_2, num_3, num_4, num_5)

def compute(first, second, third, fourth, fifth):
    addition = first + second + third + fourth + fifth
    multiplication = first * second * third * fourth * fifth
    return addition, multiplication


main()

# Code 4
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

# Code 5
def add(x, y):
    z = x + y
    return z

num1 = int(input("Ent 1: "))
num2 = int(input("Ent 2: "))
sum = add(num1, num2)

print("The sum of", num1, "and", num2, "is", sum)
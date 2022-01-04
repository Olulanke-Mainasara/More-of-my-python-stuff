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
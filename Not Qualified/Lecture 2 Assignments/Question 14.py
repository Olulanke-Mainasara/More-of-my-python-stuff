# Compound interest of a bank
p = float(input("Enter the principal amount: "))
r = float(input("Enter the annual interest rate: "))
n = float(input("Enter the number of times per year that the interest is compounded: "))
t = float(input("Enter the number of years the account will be left to earn interest: "))
R = r/100
P = (1+(R/n))**(n*t)
A = p*P
print("The amount of money in the account will be", A)

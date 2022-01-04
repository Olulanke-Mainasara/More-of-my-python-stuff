#Program to calculate the total amount of a meal

chargeforfood = int(input("Enter the charge for the food: "))
amountoftip = chargeforfood + (chargeforfood * 0.18)
amountoftax = chargeforfood + (chargeforfood * 0.07)
totalamount = amountoftip + amountoftax
print("The amount of an 18% tip is:",amountoftip)
print("The amount of a 7% sales tax is:",amountoftax)
print("The total amount is:",totalamount)
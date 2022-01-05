#Program to calculate the total amount of purchase and how much each instalment costs

amountofpurchase = int(input("Enter the amount of purchase: "))
noofpayinstalments = int(input("Enter the number of payment instalments: "))
totalamount = amountofpurchase + (0.05 * amountofpurchase)
costofinstalments = totalamount / noofpayinstalments
print("The total amount of purchase is:",totalamount)
print("The cost of each instalment is:",costofinstalments)
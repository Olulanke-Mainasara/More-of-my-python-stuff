#Program to calculate item prices and the total amount

item1 = float(input("Enter the price of the first item: "))
item2 = float(input("Enter the price of the second item: "))
item3 = float(input("Enter the price of the third item: "))
item4 = float(input("Enter the price of the fourth item: "))
item5 = float(input("Enter the price of the fifth item: "))
subtotalofsale = item1 + item2 + item3 + item4 + item5
print("The subtotal of the sale is:$",subtotalofsale)

#Program to calculate the item sales tax and total

item1tax = item1 * 0.07
item2tax = item2 * 0.07
item3tax = item3 * 0.07
item4tax = item4 * 0.07
item5tax = item5 * 0.07
taxtotalforsale = item1tax + item2tax + item3tax + item4tax + item5tax
print("The total tax for the sale is:$",taxtotalforsale)

#Program to calculate the total for the sale

totalforthesale = subtotalofsale + taxtotalforsale
print("The complete total for the sale is:$",totalforthesale)
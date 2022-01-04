#Question 1

#program to print my information
#declare your variables

name = input("Enter your name: ")
address = input("Enter yor address: ")
city = input("Enter your city: ")
state = input("Enter your state name: ")
zip = input("Enter your zip code: ")
telephoneno = input("Enter your telephone number: ")
collegemajor = input("Enter your college major: ")

print ("\nmy name is",name,"\nmy address is",address,"\nI live in the city of",city,"\nI stay in",state,"state","\nmy zip code is",zip,"\nmy telephone number is",telephoneno,"\nmy college major is",collegemajor)


#Question 2

#Program to calculate estimated profit

totalsales = float(input("Enter your projected amount of sales: "))
profit = totalsales * 0.23
print ("Your estimated profit is: ", profit)


#Question 3

#Program to calculate and display the mass of an object in kilograms

massinpounds = float(input("What is the mass in pounds: "))
massinkilograms = massinpounds * 0.454
print("The mass of the object in kilograms is: ",massinkilograms,"Kg")


#Question 4

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


#Question 5

#Program to calculate the distance a car travels

carspeed = 70

#distance = carspeed * time

distance1 = carspeed * 6
distance2 = carspeed * 10
distance3 = carspeed * 15

print("The first distnce covered is",distance1,"metres")
print("The second distance covered is",distance2,"metres")
print("The third distance covered is",distance3,"metres")

#Question 6

#Program to calculate the total amount of purchase and how much each instalment costs

amountofpurchase = int(input("Enter the amount of purchase: "))
noofpayinstalments = int(input("Enter the number of payment instalments: "))
totalamount = amountofpurchase + (0.05 * amountofpurchase)
costofinstalments = totalamount / noofpayinstalments
print("The total amount of purchase is:",totalamount)
print("The cost of each instalment is:",costofinstalments)


#Question 7

#Program to calculate the MPG of a car

noofmiles = int(input("Enter the number of miles driven: "))
gallonsofgas = int(input("Enter the gallons of gas used: "))

#MPG = Miles driven / Gallons of gas used
MPG = noofmiles / gallonsofgas
print("The MPG of the car is",MPG)


#Question 8

#Program to calculate the total amount of a meal

chargeforfood = int(input("Enter the charge for the food: "))
amountoftip = chargeforfood + (chargeforfood * 0.18)
amountoftax = chargeforfood + (chargeforfood * 0.07)
totalamount = amountoftip + amountoftax
print("The amount of an 18% tip is:",amountoftip)
print("The amount of a 7% sales tax is:",amountoftax)
print("The total amount is:",totalamount)


#Question 9

import math
#Program to calculate the area and circumference of a circle

radiusofcircle = float(input("Enter the radius of the circle: "))
area = math.pi * (radiusofcircle * radiusofcircle)
circumference = 2 * math.pi * radiusofcircle
print("The area of the circle is",area)
print("The circumference of the circle is",circumference)

#Question 10

# Ingredient adjuster
cookiesno = int(input("How many cookies do you want to bake? "))
sugaramount = cookies*0.031
butteramount = 0.021*cookies
flouramount = cookies*0.057
print("You need...")
print(sugaramount, "cup(s) of sugar")
print(butteramount, "cup(s) of butter")
print(flouramount, "cup(s) of flour")
print("to make", cookiesno, "cookies")


#Question 11

# Male and Female percentages
male = float(input("Enter the number of male students within the class: "))
female = float(input("Enter the number of females students within the class: "))
total = male + female
mpercent = (male/total)*100
fpercent = (female/total)*100
print(mpercent, "percent of the students are male")
print(fpercent, "percent of the students are female")

#Question 12

# Stock Transaction program
print("Joe brought 2000 shares at a rate of $40")
shares_1 = 2000*40
commission_1 = shares_1*0.03
print("Joe brought his shares for", shares_1)
print("and at a commission of 3% to the stockbroker he paid", commission_1)
print("Two weeks later Joe sold his 2000 shares at a rate of $42.75")
shares_2 = 2000*42.75
commission_2 = shares_2*0.03
print("Joe received", shares2, "after selling")
print("and paid his stockbroker 3% of these sales")
print("Joe paid his stockbroker", commission_2)
amountleft1 = shares_1 - commission_1
amountleft2 = shares_2 - commission_2
print("After paying the stock broker when buying the shares. Joe was left with", amountleft1)
print("After selling the shares and paying the stock broker, Joe had", amountleft2, "left")
profit = amountleft2-amountleft1
print("Joe made a profit of", profit, "dollars")


#Question 13

# Planting Grapevines
r = float(input("Input the length of the row in feet: "))
e = float(input("Input the amount of space used by an endpoint assembly in feet: "))
s = float(input("Input the amount of space between the vines in feet: "))
v = (r-(2*e))/s
print(v, "grapevines will fit in the row")


#Question 14

# Compound interest of a bank
p = float(input("Enter the principal amount: "))
r = float(input("Enter the annual interest rate: "))
n = float(input("Enter the number of times per year that the interest is compounded: "))
t = float(input("Enter the number of years the account will be left to earn interest: "))
R = r/100
P = (1+(R/n))**(n*t)
A = p*P
print("The amount of money in the account will be", A)



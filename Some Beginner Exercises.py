#Question1
def main():
    print("Welcome")
    distance()
    print("Goodbye")
def distance():
    Kilometres= float(input("Please enter the distance in kilometres:"))
    miles=Kilometres*0.6214
    print("Distance travelled in miles is:",miles)
mainone()

#Question2
def main():
    print("Welcome")
    repeat()
    print("Goodbye")

def repeat():
    Word = input("Enter a word please:")
    Num = int(input("Enter a number also:"))
    mutiply = Word * Num
    print(mutiply)
main()

#Question3
def main():
    print("Welcome")
    insurance()
    print("Goodbye")

def insurance():
    replace=int(input("Please enter the replacement cost:"))
    percentage=replace*0.8
    print("This is the minimum amount of insurance money need to purchase:",percentage)
main()

#Question4
def main():
    print("Welcome")
    Automobile_Costs()
    print("Goodbye")
def Automobile_Costs():
    loan_payment=int(input("Enter the loan payment amount:"))
    insurance=int(input("Enter the money put into insurance:"))
    gas=int(input("Enter the amount used in purchasing gas:"))
    oil=int(input("Enter the amount used in purchasing oil:"))
    tire=int(input("Enter the amount used in purchasing tires:"))
    maintenance=int(input("Enter the amount used for maintenance:"))
    Monthly_cost=loan_payment+insurance+gas+oil+tire+maintenance
    Annual_cost=Monthly_cost*12
    print("The monthly cost is:",Monthly_cost)
    print("The annual expense cost is:",Annual_cost)
main()

#Question5
def main():
    print("Welcome")
    assessment_value()
    print("Goodbye")

def assessment_value():
    property_val=int(input("Enter the exact amount the property was bought:"))
    assessment_val=property_val*0.6
    tax = assessment_val / 100*0.72
    print("The Assessment Values is:",assessment_val)
    print("The Tax Values is:", tax)
main()

#Question6
def main():
    print("Welcome")
    Name=input("Please enter your name:")
    Member=int(input("Please enter your memebership Id:"))
    cal()
    carbs()
    print("Goodbye")

def cal():
    Fat_grams=int(input("Please enter the number of fat grams you take per day:"))
    Calories=Fat_grams*9
    print("You gain this amount",Calories,"from fat")
def carbs():
    carbs_grams=int(input("Please enter the number of carbohydrate grams you take per day:"))
    cal_carbs=carbs_grams*4
    print("You gain this amount",cal_carbs, "from carbohydrates")
main()

#Question7
def main():
    print("Welcome")
    FunctionA()
    FunctionB()
    FunctionC()
    print("Goodbye")

def FunctionA():
    Class_A=int(input("Please enter the number of tickets sold for class A seats:"))
    Class_A_income=Class_A*20
    print("The total income generated from Class A is:",Class_A_income)

def FunctionB():
    Class_B = int(input("Please enter the number of tickets sold for class B seats:"))
    Class_B_income = Class_B *15
    print("The total income generated from Class B is:", Class_B_income)

def FunctionC():
    Class_C = int(input("Please enter the number of tickets sold for class C seats:"))
    Class_C_income = Class_C * 20
    print("The total income generated from Class A is:", Class_C_income)
main()

#Question8
def main():
    print("Good day")
    paint_job_estimate()
    print("Goodbye")

def paint_job_estimate():
    square_feet = float(input('Enter the square feet of wall to be painted: '))
    paint_price = float(input('Enter the price per gallon of paint: '))
    gallon_of_paint = square_feet / 112
    hours_worked = (square_feet / 112) * 8
    cost_of_paint = paint_price * gallon_of_paint
    labour_charges = 35 * hours_worked
    total_cost = cost_of_paint + labour_charges
    print('The number of gallons of paint required is:',gallon_of_paint)
    print('The hours of labour required is:',hours_worked)
    print('The cost of the paint is:',cost_of_paint)
    print('The labour charges are:',labour_charges)
    print('The total cost of the paint job is:',total_cost)
main()


#Question9
def main():
    print("Welcome")
    Tax()
    print("Goodbye")

def Tax():
    Sales = int(input("Please enter the total sales of the month:"))
    Sales_tax = Sales * 0.5
    print("The state sales tax rate is:", Sales_tax)
    County_sales=Sales*0.025
    print("The county sales tax rate is",County_sales)
    Total_sales= Sales_tax+County_sales
    print("The total sales tax calculated is",Total_sales)
main()

#Question10
def main():
    print("Welcome")
    Feets_to_inches(2)
    print("Goodbye")

def Feets_to_inches(feets):
    f_to_i= feets*12
    print("The number of inches in the Foot typed in is:",f_to_i)
main()

#Question11
def main():
    print("Good day")
    Addition()
    print("Goodbye")
def Addition():
    import random
    for i in range(1,6):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        sum=num1+num2
        print("Question",i)
        print(num1,"+",num2,"=",sum)

main()

#Question12
def main():
    print("Welcome")
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter a number:"))
    max(num1,num2)
    print("Goodbye")

def max(A,B):
    if A>B:
        print(A)
    elif A==B:
        print("None is greater")
    else:
        print(B)
main()

#Question13
def falling_distance(time):
    g=9.8
    distance=0.5*g*(time**2)
    print(distance)

for i in range(1,11):
    falling_distance(i)


#Question14
def main():
    print("Welcome")
    MassInput = float(input("Enter the mass of the object(in Kg):"))
    VelocityInput = float(input("Enter the velocity of the object in(meter per second):"))
    Kinetic_energy(MassInput,VelocityInput)
    print("Goodbye")

def Kinetic_energy(M,V):
    K_E=1/2*M*(V**2)
    print("The Kinetic energy of the object is:",K_E)
main()

#Question15
def main():
    Name=input("Enter Your Name:")
    Matric=input("Enter Your Matric Number:")
    T1=int(input("Enter Your First Test Score:"))
    T2=int(input("Enter Your Second Test Score:"))
    T3=int(input("Enter Your Third Test Score:"))
    T4=int(input("Enter Your Fourth Test Score:"))
    T5=int(input("Enter Your Fifth Test Score:"))
    Calc_Average(T1,T2,T3,T4,T5)
    print("")
    print("Let's determine you grade")
    T = int(input("Enter your test score:"))
    Determine_grade(T)
    print("Goodbye")

def Calc_Average(Test1,Test2,Test3,Test4,Test5):
    Avrg= Test1+Test2+Test3+Test4+Test5/5
    print("The Average of your test scores is:",Avrg)

def Determine_grade(Test):
    if Test >= 90 and Test == 100:
        print("A")
    elif Test >= 80 and Test < 90:
        print("B")
    elif Test >= 70 and Test < 80:
        print("C")
    elif Test >= 60 and Test < 70:
        print("D")
    else:
        print("You got an F")
        print("You can always chose to rewrite")
main()

#Question16
def main():
    print("Let get the odd and even numbers from 1 to 100")
    counter()

def counter():
    import random
    odd_counter = 0
    even_counter = 0
    for i in range(0, 100):
        num = random.randint(1, 100)
        if num % 2 == 0:
            print(num, 'This is even')
            even_counter += 1
        else:
            print(num, 'This is odd')
            odd_counter += 1

    print('There are',odd_counter,'odd numbers')
    print('There are',even_counter,'even numbers')
main()

#Question17
"""A prime number is a positive integer that is only divisible by 1 and itself"""
def is_prime(number):
    if number == 1:
        return True
    for i in range(2, number):  # This checks if the specified number is divisible by 2 or any other besides itself
        if number % i == 0:
            return False  # If it is divisible then it is not a prime number
    return True


prime_number_prompt = int(input('Enter an integer number: '))
if is_prime(prime_number_prompt):
    print('This is a prime number')
else:
    print('This is not a prime number')

#Question18
def is_prime(value):
    if value== 1:
        return True
    for i in range(2, value)
        if value % i == 0:
            return False
    return value

for i in range(1, 101):
    value = is_prime(i)
    if value
        print(value)

main()
#Question19
def main():
    print("Welcome")
    Loan()
    print("Goodbye")

def Loan():
    A=int(input("Please input the loan amount:"))
    M=int(input("Please input the number of month needed:"))
    R=int(input("The monthly interest rate in per centage:"))
    Top=(R/100)*A
    Low=1-(1+R)**-M
    P=Top/Low
    print("The monthly payment necessary is:",P)
main()

#Question20
import random
def main():
    print("Welcome to Guess game")
    guessing_games()
    print("Goodbye")
def guessing_games():
    guess_round=1
    random_number=random.randint(1,100)
    Rerun="Y"
    while Rerun=="Y" or Rerun=="y":
        guess=int(input("Guess the number:"))
        if guess==random_number:
            print("Congratulations!!!", end='')
            if guess_round==1:
                print("You won on your first guess congratulations")
            else:
                print("You guessed",guess_round,"times")

            Rerun=input("Do you wish to keep playing press 'Y or N':")
            if Rerun=="Y" or Rerun=="y":
                guessing_games()

        elif guess>random_number:
            print("Too high, try again")
            guess_round+=1
            Rerun = input("Press 'Y or y' to continue guessing?")

        else:
            print("Too low,try again")
            guess_round+=1
            Rerun = input("Press 'Y or y' to continue guessing?")
    print('Thanks for playing')
main()


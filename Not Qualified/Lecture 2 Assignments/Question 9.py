import math
#Program to calculate the area and circumference of a circle

radiusofcircle = float(input("Enter the radius of the circle: "))
area = math.pi * (radiusofcircle * radiusofcircle)
circumference = 2 * math.pi * radiusofcircle
print("The area of the circle is",area)
print("The circumference of the circle is",circumference)

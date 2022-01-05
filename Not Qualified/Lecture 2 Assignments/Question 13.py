# Planting Grapevines
r = float(input("Input the length of the row in feet: "))
e = float(input("Input the amount of space used by an endpoint assembly in feet: "))
s = float(input("Input the amount of space between the vines in feet: "))
v = (r-(2*e))/s
print(v, "grapevines will fit in the row")

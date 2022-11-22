import math
x = float(input("Enter the number: "))
if -1 <= x and x <= 1 :
    t = math.atan(x)
    print("Angles in radians: ","{0:.3f}".format(t))
    print("Angles in degrees: ",math.degrees(t))
else : print("Invalid Input")
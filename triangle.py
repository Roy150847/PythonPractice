

a = int(input("Enter the first side:"))
b = int(input("Enter the second side:"))
c = int(input("Enter the third side:"))



if a >= b and a >= c :
    if b + c > a:
        print(" Triangle is possible ")
    else :
        print(" Triangle is not possible")
elif b >= a and b >= c :
    if a + c > b:
        print(" Triangle is possible ")
    else :
        print(" Triangle is not possible")
elif c >= a and c >= b :
    if a + b > c :
        print(" Triangle is possible ")
    else :
        print(" Triangle is not possible")
else :
    print(" Triangle is not possible")




# The above program in one line
'''
if (a >= b and a >= c and b + c > a) or (b >= a and b >= c and a + c > b) or (c >= a and c >= b and a + b > c) :
    print(" Triangle is possible")
else :
    print("Triangle is not possible")
'''
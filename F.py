#y = float(input("Enter y:"))
#print("{0:.4f}".format(y))

N = int(input())
l = N % 10
f = N // 1000
if f % 2 != 0 and l % 2 != 0 :
    print("True")
else :
    print("False")
n = int(input(" Enter the value of n upto which you want to print the series :"))
n1, n2 = 0, 1
print(str(n1) + ", " + str(n2), end = ", ")
'''
for i in range(n-2) :
    n3 = n1 + n2
    print(n3, end=", ")
    n1 = n2
    n2 = n3
'''
for i in range(n-2) :
    n3 = n1 + n2
    if i != n - 3:
        print(n3, end=", ")
    else :
        print(n3)
    n1 = n2
    n2 = n3

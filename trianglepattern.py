def triangle(n) :
    for i in range(0, n):
        for j in range(1,n-i):
            print(end=" ")
        for k in range(0, i+1):
            print("*", end=" ")
        print("\r")
n = int(input("Enter the value of n: "))
triangle(n)
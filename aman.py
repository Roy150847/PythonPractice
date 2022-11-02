n = int(input())
d = n % 10
if d % 2 != 0:
    print(str(n)[0:-1]+"o")
else :
    print(n)
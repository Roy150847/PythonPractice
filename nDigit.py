n = int(input(" Enter the number :"))
'''
while n>=1:
    d = n % 10
    n = n // 10
    print(d)
'''
l = len(str(n))
for i in range(l):
    dig = (n%(i+1)-n%(10**i))//10**i
    print(dig)
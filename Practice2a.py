n1 = int(input())
n2 = int(input())
for i in range(n1,n2+1) :
    factor = 0
    for j in range(1,i+1) :
        if (i%j)==0:
            factor = factor + 1
    if factor == 2 :
        print(i)
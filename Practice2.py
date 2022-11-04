start = int(input("Enter the start of range:"))
end = int(input("Enter the end of range:"))
for i in range(start,end+1) :
    factor = 0
    for j in range(1,i+1) :
        if (i%j)==0:
            factor = factor + 1
    if factor == 2 :
        print(i)
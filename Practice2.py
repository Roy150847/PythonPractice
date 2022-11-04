start = int(input("Enter the start of range:"))
end = int(input("Enter the end of range:"))
factor = 0
i = start
j = 1
while i <= end :
    while j <= i :
        if i%j==0:
            factor = factor + 1
        j = j+1
    if factor == 2 :
        print(j)
    i=i+1

start = int(input("Enter the start of range:"))
end = int(input("Enter the end of range:"))
print("The prime numbers in the range are:")
for i in range(start,end+1) :
    if i > 1:
        for j in range(2,i) :
            if (i%j) == 0 :
                break
        else:
            print(i)
a = int(input(" Enter the number: "))
if a > 99 and a < 1000 :
    print(" Number on unit's place is :",end=" ")
    print(a%10)
    print(" Number on ten's place is :",end=" ")
    print(int((a%100-a%10)/10))
    print(" Number on hundred's place is :",end=" ")
    print((a-a%100)//100)
else :
    print(" Number is not three digit ")
from tkinter import N


num = int(input("Enter the number:"))
s = num
l = len(str(num))
sum = 0
while num!=0:
    r = num % 10
    sum = sum + (r ** l)
    num = num//10
if s == sum:
    print("The given number is armstrong")
else :
    print("The given jumber is not armstrong")
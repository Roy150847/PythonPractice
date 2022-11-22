# PROGRAM TO CHECK IF A NUMBER IS IN FIBONACCI SERIES OR NOT

def fibonacci(num):
    a = 0
    b = 1
    if num == 0 or num == 1 :
        return 1
    while b <= num :
        c = a + b
        a = b
        b = c
        if c == num:
            return 1
            break

number = int(input("Enter the number: "))
if fibonacci(number) == 1 :
    print("The given number is in Fibonacci Series")
else :
    print("The given number is not in Fibonacci series")
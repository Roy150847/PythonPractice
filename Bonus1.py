sal = int(input("Enter the salary:"))
time = int(input("Enter the time spent:"))
if time >= 10 :
    bonus = 0.10 * sal
    print("Bonus is:",bonus)
    print("Total Salary is:",bonus+sal)
elif time >=6 and time < 10 :
    bonus = 0.08 * sal
    print("Bonus is:",bonus)
    print("Total Salary is:",bonus+sal)
elif time < 6 :
    bonus = 0.05 * sal
    print("Bonus is:",bonus)
    print("Total Salary is:",bonus+sal)
else :
    print("Invalid input")
    
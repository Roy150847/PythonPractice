n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))
list = n1, n2,n3
largest = 0
for i in list :
    if i > largest :
        largest = i

print("Largest:",largest)
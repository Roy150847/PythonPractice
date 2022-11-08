s1 = input()
s2 = input()
l1 = s1[0]
l2 = s2[0]
s = 0
for i in range(len(s2)) :
    if l1 == s2[i] :
        for j in range(len(s2)) :
            if l2 == s2[j] :
                s = s + 1
                print("True")
                break

if s == 0 :
    print("False")
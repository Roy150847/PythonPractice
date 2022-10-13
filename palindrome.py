x = str(input(" Enter the word to be checked :"))
n = len(x)
if(n % 2 == 0) :
    for i in range(0, n/2):
        if x[i] != x[n-i-1] :
            break
            print(" It's a plindrome ")
        else :
            print(" It's not a palindrome ")
else :
    n1 = int(n/2)
    for i in range(0, n1):
        if x[i] != x[2 * n1 -i-1] :
            break
            print(" It's a plindrome ")
        else :
            print(" It's not a palindrome ")


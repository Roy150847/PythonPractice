

str = str(input(" Enter the string to be checked :"))

'''
def Palindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

ans = Palindrome(str)
if ans == False :
    print("It's not a palindrome")
else :
    print("It's a palindrome")
'''


rev = str[::-1]
if(rev == str):
    print("It's a palindrome")
else :
    print("It's not a palindrome")

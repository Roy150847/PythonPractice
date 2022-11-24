def find_char(str1,char):
    x = "not found"
    if char in str1:
        if (str1.index(char)+1) < len(str1):
            return str1.index(char)+1
        else:
            return x
    else :
        return x

str1 = input("Enter the string: ")
char = input("Enter the charcter to be found: ")
print(find_char(str1,char))
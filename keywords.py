import keyword
str = input(" Enter the string to be checked: ")
if keyword.iskeyword(str)== True:
    print(str+" is a keyword")
else :
    print(str+" is not a keyword")

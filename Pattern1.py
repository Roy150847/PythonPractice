'''
A program to take a word as input and print in following pattern
word input: Python
output: 
P
Py
Pyt
Pyth
Pytho
Python
'''
str = input("Enter the word: ")
l = len(str)
res = ""
for i in str:
    res = res + i
    print(res)
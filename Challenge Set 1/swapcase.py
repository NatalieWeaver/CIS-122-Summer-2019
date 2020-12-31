'''
Author: Natalie Weaver
Date: July 3, 2019

CIS 122 Challenge Set 1 part 3: Swap Case

Sources:
    This ASCII table: https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html
'''

string = input("Input a string: ")
swapcase_string = ""

i = 0
while i < len(string):
    if string[i].isupper():
        swapchar = chr(ord(string[i]) + 32)
    elif string[i].islower():
        swapchar = chr(ord(string[i]) - 32)
    else:
        swapchar = string[i]
    swapcase_string = swapcase_string + swapchar
    i = i + 1

print("Case-swapped string:" , swapcase_string)

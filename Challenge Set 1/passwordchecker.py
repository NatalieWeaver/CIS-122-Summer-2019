'''
Author: Natalie Weaver
Date: July 3, 2019

CIS 122 Challenge Set 1 part 1: Password checker

Sources: This website on string methods: https://www.programiz.com/python-programming/methods/string
'''

def is_valid(pw):
    '''
    (str) -> boolean
    Returns True if the password is valid according to the assignment rules, and False otherwise.

    >>> is_valid("password")
    False
    (lacks numbers, special character, capital)

    >>>is_valid("P45$w0rd")
    True
    '''
    # first, we find the number of numbers in the password:
    digits = "0123456789"
    numbers = 0
    for char in pw:
        if char in digits:
            numbers = numbers + 1

    # now we test all the conditions for a valid password:
    if len(pw) < 8:
        print("Passwords must have at least 8 characters.")
        return False
    elif numbers < 3:
        print("Passwords must contain at least 3 numbers.")
        return False
    elif pw.isalnum():
        print("Passwords must contain at least one special character.")
        return False
    elif pw.islower():
        print("Passwords must contain at least one capital letter.")
    else:
        return True

# ask for the user's initial choice of password
password = input("Please enter your password: ")

# make them keep trying until they choose a valid password
while not is_valid(password):
    password = input("Please enter your password: ")

# we only get to this line when we input a valid password:
print("Hooray! Your password is valid!")

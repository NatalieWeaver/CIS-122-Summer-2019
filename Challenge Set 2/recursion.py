'''
Author: Natalie Weaver
Date:   July 9, 2019

CIS 122 Challenge Set 2
Countdown, factorial, and string reverse functions written by recursion.

Sources: None
'''

def countdown(start):
    '''
    (int) -> None
    Takes a non-negative integer and prints a countdown from that integer to 0, inclusive.

    >>> countdown(0)
    0

    >> countdown(3)
    3
    2
    1
    0
    '''

    if start < 0:
        print("Only countdown from non-negative numbers")
        return

    if (start % 1) != 0:
        print("Only countdown from integers")
        return
    
    if start == 0:
        print(0)
        return

    print(start)
    countdown(start - 1)

def factorial_r(num):
    '''
    (int) -> int
    Takes a non-negative integer and returns the factorial of that integer.

    >>> factorial_r(0)
    1

    >>> factorial_r(1)
    1

    >>> factorial_r(4)
    24
    '''

    if (num % 1) != 0 or num < 0:
        print("Only take the factorial of non-negative integers")
        return

    if num == 0:
        return 1

    return num * factorial_r(num - 1)

def str_reverse_r(string):
    '''
    (str) -> str
    Takes a string and returns its reverse (by recursion).

    >>> str_reverse_r("hello")
    olleh
    '''

    if len(string) == 1:
        return string

    reverse = string[-1]
    newstring = string[ :-1]
    reverse = reverse + str_reverse_r(newstring)
   
    return reverse

    

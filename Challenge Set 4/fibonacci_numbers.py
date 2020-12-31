'''
Author: Natalie Weaver
Date:   July 30, 2019

CIS 122 Challenge Set 4 Part 1
Function for the nth fibonacci number, done by recursion

Sources: None
'''

def fib(n):
    '''
    (int) -> int
    Returns the nth fibonacci number.

    >>> fib(1)
    0

    >>> fib(2)
    1

    >>> fib(3)
    1

    >>> fib(4)
    2
    '''

    if n == 1:
        return 0

    if n == 2:
        return 1

    return fib(n - 2) + fib(n - 1)

for i in range(1, 10):
    print(fib(i))

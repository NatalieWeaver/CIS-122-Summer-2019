'''
Author: Natalie Weaver
Date:   July 30, 2019

CIS 122 Challenge Set 4 Part 2
Bubble sorting function

Sources: None
'''

def bubblesort(li):
    '''
    (list) -> None
    Uses the bubble sorting algorithm to sort lists in place.

    >>> numbers = [2, 1, 4, 3]
    >>> bubblesort(numbers)
    >>> numbers
    [1, 2, 3, 4]
    '''
    
    for i in range(1, len(li)):
        while (li[i] < li[i - 1]) and (i > 0):
            temp = li[i - 1]
            li[i - 1] = li[i]
            li[i] = temp
            i = i - 1

    return None

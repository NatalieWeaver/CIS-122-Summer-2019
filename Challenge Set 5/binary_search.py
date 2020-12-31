'''
Author: Natalie Weaver
Date:   August 2, 2019

CIS 122 Challenge Set 5
Implementing binary search algorithms iteratively and recursively.

Sources: None
'''

def binary_search_iterative(li, target):
    '''
    (list, object) -> boolean
    Returns true if target is an element of the list, False otherwise.

    examples
    '''

    if li == []:
        return False

    li.sort()
    index = len(li) // 2
    lower_bound = 0
    upper_bound = len(li) - 1
    # print("index: ", index, "; lower: ", lower_bound, "; upper: ", upper_bound)

    while li[index] != target:
        
        if target < li[index]:
            upper_bound = index
            index = index // 2

        elif target > li[index]:
            lower_bound = index
            index = index // 2 + index

        if index == index // 2:        # i.e. if index is already 0
            return False
        if index < lower_bound:
            return False
        if index > upper_bound:
            return False

        # print("index: ", index, "; lower: ", lower_bound, "; upper: ", upper_bound)

    return True

# first, sort the list
# compare target to middle element. either target == middle element, target > middle, or target < middle.
# if target == middle element, return True (we never enter the while loop)
# if target != middle element, we need to make another comparison:
# if target < middle, compare to element halfway between beginning and middle, index = middle // 2
# if target > middle, compare to element halfway between middle and end, index = middle + middle // 2
# while we haven't found target in the list yet, keep doing this using a while loop
# at some point, either target == li[index], so we exit the loop and return True
# or our index will always be 0 or goes out of range, which means target < minimum or target > maximum.
# in either case, return False. We need to check these indices each time the loop is executed
# to avoid getting an index error.

print(binary_search_iterative([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
print(binary_search_iterative([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 24))
print(binary_search_iterative(["soccer", "basketball", "hockey", "dance", "baseball", "unicycling"], "running"))
print(binary_search_iterative(["soccer", "basketball", "hockey", "dance", "baseball", "unicycling"], "soccer"))


def binary_search_recursive(li, target):
    '''
    (list, object) -> boolean
    Returns true if target is an element of the list, False otherwise.

    examples
    '''

    if li == []:
        return False
    
    li.sort()
    middle = len(li) // 2

    if target == li[middle]:
        return True

    if target < li[middle]:
        half_list = li[ : middle]
        # print(half_list)
        return binary_search_recursive(half_list, target)

    if target > li[middle]:
        if middle == len(li):
            half_list = []
        else:
            half_list = li[middle + 1 : ]
        # print(half_list)
        return binary_search_recursive(half_list, target)


# first, sort the list
# compare target to middle element. return True if they are the same
# if not the same, either target < middle or target > middle.
# In the first case, new list of elements before middle
# Second case, new list of elements after middle
# repeat with new list
# if list is ever empty, we failed to find a match, so return False

print(binary_search_recursive([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
print(binary_search_recursive([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 24))
print(binary_search_recursive(["soccer", "basketball", "hockey", "dance", "baseball", "unicycling"], "running"))
print(binary_search_recursive(["soccer", "basketball", "hockey", "dance", "baseball", "unicycling"], "soccer"))


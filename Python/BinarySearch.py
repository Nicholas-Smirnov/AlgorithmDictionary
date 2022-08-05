# A binary search is a beautiful and simple algorithm
# that can be used to find a value in a sorted list.

# The binary search algorithm is O(log n)
# The binary search algorithm is a recursive algorithm
# that divides the list into two halves, and then
# searches the halves recursively.

import math

COUNT = 0

def BinarySearch(myList, val):

    global COUNT
    COUNT += 1

    INDEX = math.floor(len(myList) / 2)

    if len(myList) == 1:
        return myList[0]

    if myList[INDEX] == val:
        return myList[INDEX]
    elif myList[INDEX] > val:
        myList = myList[:INDEX]
    elif myList[INDEX] < val:
        myList = myList[INDEX:]

    return BinarySearch(myList, val)

BinarySearch([i for i in range(10000)], 4)
print(COUNT)

# Created by Nicholas Smirnov

# A linear search is the simplest search algorithm.
# It iterates through the list and checks each element
# to see if it matches the target.

# This is the linear search algorithm.
# It has an O(n) runtime.

def LinearSearch(myList, target):
    INDEX = 0
    for i in myList:
        if i == target:
            return INDEX
        INDEX += 1
    return -1

# Created by Nicholas Smirnov

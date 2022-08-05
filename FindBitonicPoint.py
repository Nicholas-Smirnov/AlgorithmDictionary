# A bitonic list is a list that increases to a certain
# point and then decreases from that point to the end 
# of the list.

# This bitonic algorithm is O(log n)
# This is because it uses the binary search
# algorithm to find the bitonic point.

import math

def FindBitonicPoint(myList):

    COUNT = 0

    while True:

        INDEX = math.floor(len(myList) / 2)
        COUNT += 1

        if len(myList) == 1:
            return myList[0]

        print(INDEX)
        print(myList)

        if myList[INDEX-1] > myList[INDEX]:
            myList = myList[:INDEX]
        elif myList[INDEX-1] < myList[INDEX]:
            myList = myList[INDEX:]


# This is an example of a bitonic list: [3, 4, 11, 8, 6, 5, 4]
# The bitonic point is 11.

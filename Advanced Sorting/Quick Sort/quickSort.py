
# Sorts an array or list using the recursive quick sort algorithm.
def quickSort( theSeq ) :
    n = len( theSeq )
    recQuickSort( theSeq, 0, n - 1 )

# The recursive implementation using virtual segments.
def recQuickSort( theSeq, first, last ) :
    # Check the base case.
    if first >= last :
        return

    else :
        # Save the pivot value.
        pivot = theSeq[ first ]

        # Partition the sequence and obtain the pivot position.
        pos = partitionSeq( theSeq, first, last )

        # Repeat the process on the two subsequences.
        recQuickSort( theSeq, first, pos - 1 )
        recQuickSort( theSeq, pos + 1, last )

# Partitions the subsequence using the first key as the pivot.
def partitionSeq( theSeq, first, last ) :
    # Save a copy of the pivot value.
    pivot = theSeq[ first ]

    # Find the pivot position and move the elements around the pivot.
    left = first + 1
    right = last

    while left <= right :
        # Find the first key larget than the pivot.
        while left < right and theSeq[ left ] < pivot :
            left += 1

        # Find the last key in the sequence that is smaller than the pivot.
        while right >= left and theSeq[ right ] >= pivot :
            right -= 1

        # Swap the two keys if we have not completed this partition.
        if left < right :
            theSeq[ left ], theSeq[ right ] = theSeq[ right ], theSeq[ left ]

    # Put the pivot in the proper position.
    if right != first :
        theSeq[ first ] = theSeq[ right ]
        theSeq[ right ] = pivot

    # Return the index position of the pivot value.
    return right

mySeq = [ 10, 23, 51, 18, 4, 31, 5, 13, 39, 38, 29, 39, 392, 3892, 37, 3892, 2983, 9283, 8329, 3928, 9283, 283, 8298, 9283, 9283, 838, 497, 489, 9384, 743, 9834, 53, 44, 645, 324, 564, 654, 567, 645, 54, 3, 64, 65, 545, 645, 656, 7675, 645, 6524, 634, 6243, 7545, 5776, 53, 54, 425, 4234, 657, 5686, 656, 6356654, 74, 54, 2, 34, 57,676, 567, 86, 56, 5443, 56, 4423, 65, 76, 9, 7565, 56, 453, 54, 54, 3432, 2, 1, 43, 6, 54, 5654, 5354, 5, 4234, 65, 453, 452, 142, 654, 53, 432, 45, 424, 366, 76, 5888866, 765, 98, 56345, 4523, 75, 45, 345, 56, 543, 234, 1,3212, 123, 654, 345, 54, 754, 434, 32454, 366, 434, 42, 313, 341, 645, 74, 56345, 523456547653, 42, 43143, 3123, 4345, 453, 634, 453, 4234, 4345, 65, 2, 87, 8765, 757, 4567, 645, 78, 967,8 ,765, 0, 86890, 764, 365, 254, 4524, 564, 74563, 24, 5245, 4234, 42345, 4235, 564,6 ,76456, 8974853 ,524, 7654 ]
print( len( mySeq ) )
quickSort( mySeq )
print( mySeq )
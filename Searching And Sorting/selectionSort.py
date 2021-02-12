
# Implementation of the selection sort algorithm.
def selectionSort( theSeq ) :
    n = len( theSeq ) 

    # Find the smallest value's index.
    for i in range( n - 1 ) :
        # Assume the ith element is the smallest.
        smallIndex = i
        # Go through the unsorted part of the sequence.
        for j in range( i + 1, n ) :
            if theSeq[j] < theSeq[smallIndex] :
                smallIndex = j

        # Swap the ith value and smallNdx value only if the smallest value is
        # not already in its proper position. Some implementations omit testing
        # the condition and always swap the two values.
        if smallIndex != i :
            theSeq[i], theSeq[smallIndex] = theSeq[smallIndex], theSeq[i]

    return theSeq

myList = [15, 2, 11, 5, 2, 20]
print( selectionSort( myList ) )


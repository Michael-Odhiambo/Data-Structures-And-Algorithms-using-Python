

# Implementation of the insertion sort algorithm.
def insertionSort( theSeq ) :
    n = len( theSeq )

    # Start with the first value as the only 
    # sorted value.
    for i in range( 1, n ) :
        # Save the value to be positioned.
        value = theSeq[i]
        # Find the position where the value fits in
        # the sorted part of the list.
        pos = i
        while pos > 0 and value < theSeq[ pos - 1 ] :
            theSeq[ pos ] = theSeq[ pos - 1 ]
            pos -= 1

        theSeq[pos] = value

    return theSeq





















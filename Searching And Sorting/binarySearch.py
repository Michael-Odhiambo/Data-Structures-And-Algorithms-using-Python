
# Implementation of the binary search algorithm.
def binarySearch( theValues, target ) :
    # Start with the entire sequence of elements.
    high = len( theValues ) - 1
    low = 0

    # Repeatedly subdivide the sequence in half until the 
    # target is found.
    while low <= high :
        # Find the midpoint of the sequence.
        mid = ( high + low ) // 2
        # Does the midpoint contain the target?
        if theValues[mid] == target :
            return True
        # Or does the value precede the midpoint.
        elif theValues[mid] < target :
            low = mid + 1
        # Or does it follow the midpoint.
        else :
            high = mid - 1

    # If the sequence cannot be subdivided further, we're done.
    return False



    
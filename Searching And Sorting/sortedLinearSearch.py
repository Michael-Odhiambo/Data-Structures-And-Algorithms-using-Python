
# Performs a linear search on a sorted sequence.
def sortedLinearSearch( theList, item ) :
    n = len( theList )

    for i in range( n ) :
        if theList[i] == item :
            return True

        elif theList[i] > item :
            return False

    return False

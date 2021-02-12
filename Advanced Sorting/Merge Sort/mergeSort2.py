
from arrayADT import Array


# Sorts a virtual subsequence in ascending order using the merge sort algorithm.
def recMergeSort( theSeq, first, last, tmpArray ) :

    # The elements that comprise the virtual subsequence are indicated
    # by the range[ first ... last ]. tmpArray is temporary storage
    # used in the merging phase of the merge sort algorithm.

    # Check the base case: the virtual sequence contains a single item.
    if first == last :
        return

    else :
        # Compute the midpoint.
        mid = ( first + last ) // 2

        # Split the sequence and perform the recursive step.
        recMergeSort( theSeq, first, mid, tmpArray )
        recMergeSort( theSeq, mid + 1, last, tmpArray )

        # Merge the two ordered subsequences.
        mergeVirtualSeq( theSeq, first, mid + 1, last + 1, tmpArray )
    return theSeq
# Merges the two sorted virtual subsequences: [ left ... right) [right ... end)
# using the tmpArray for intermediate storage.
def mergeVirtualSeq( theSeq, left, right, end, tmpArray ) :

    # Initialize two subsequence index variables.
    a = left
    b = right

    # Initalize an index variable for the resulting merged array.
    m = 0

    # Merge the two sequences together until one is empty.
    while a < right and b < end :
        if theSeq[ a ] < theSeq[ b ] :
            tmpArray[ m ] = theSeq[ a ]
            a += 1

        else :
            tmpArray[ m ] = theSeq[ b ]
            b += 1

        m += 1

    # If the left subsequence contains more items, append them to the tmpArray.
    while a < right :
        tmpArray[ m ] = theSeq[ a ]
        a += 1
        m += 1

    # Or if the right subsequence contains more items, append them to tmpArray.
    while b < end :
        tmpArray[ m ] = theSeq[ b ]
        b += 1
        m += 1

    # Copy the sorted subsequence back into the original sequence structure.
    for i in range( end - left ) :
        theSeq[ i + left ] = tmpArray[ i ]

# Sorts an array or list in ascending order using merge sort.
def mergeSort( theSeq ) :
    n = len( theSeq )
    # Create a temporary array for use when merging subsequences.
    tmpArray = Array( n )
    # Call the private recursive merge sort function.
    return recMergeSort( theSeq, 0, n - 1, tmpArray )

mySequence = mySeq = [ 10, 23, 51, 18, 4, 31, 5, 13, 39, 38, 29, 39, 392, 3892, 37, 3892, 2983, 9283, 8329, 3928, 9283, 283, 8298, 9283, 9283, 838, 497, 489, 9384, 743, 9834, 53, 44, 645, 324, 564, 654, 567, 645, 54, 3, 64, 65, 545, 645, 656, 7675, 645, 6524, 634, 6243, 7545, 5776, 53, 54, 425, 4234, 657, 5686, 656, 6356654, 74, 54, 2, 34, 57,676, 567, 86, 56, 5443, 56, 4423, 65, 76, 9, 7565, 56, 453, 54, 54, 3432, 2, 1, 43, 6, 54, 5654, 5354, 5, 4234, 65, 453, 452, 142, 654, 53, 432, 45, 424, 366, 76, 5888866, 765, 98, 56345, 4523, 75, 45, 345, 56, 543, 234, 1,3212, 123, 654, 345, 54, 754, 434, 32454, 366, 434, 42, 313, 341, 645, 74, 56345, 523456547653, 42, 43143, 3123, 4345, 453, 634, 453, 4234, 4345, 65, 2, 87, 8765, 757, 4567, 645, 78, 967,8 ,765, 0, 86890, 764, 365, 254, 4524, 564, 74563, 24, 5245, 4234, 42345, 4235, 564,6 ,76456, 8974853 ,524, 7654 ]
print( mergeSort( mySequence ) )

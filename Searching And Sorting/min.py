
# Searching for the smallest value in a sequence.
def findMin( theList ) :
    # Assume the first value in the list is the smallest.
    smallest = theList[0]
    
    for i in range( 1, len( theList ) ) :
        if theList[i] < smallest :
            smallest = theList[i]

    return smallest



myList = [110, 30, 3, 2, 5 ]
print( findMin( myList ) )

mid = 1
while mid > 0 :
    print( "Yes" )
    mid -= 1
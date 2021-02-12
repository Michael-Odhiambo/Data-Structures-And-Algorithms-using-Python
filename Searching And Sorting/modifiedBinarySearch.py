
# Modify the binary search algorithm to find the position of the first occurrence
# of a value that can occur multiple times in the ordered list. Verify your
# algorithm is still O(log n).
def modifiedBinarySearch( theList, target ) :
    low = 0
    high = len( theList ) - 1

    while low <= high :
        mid = ( low + high ) // 2
        if theList[mid] == target :
            while mid > 0 :
                if theList[ mid - 1 ] == target :
                    mid -= 1

                else :
                    return mid

            return mid

        elif theList[mid] < target :
            low = mid + 1

        else :
            high = mid - 1 

    
myList = [ 1, 1, 1, 1, 1, 2, 3, 4, 5, 5, 5, 5, 5, 5 ]
print( modifiedBinarySearch( myList, 1 ) )
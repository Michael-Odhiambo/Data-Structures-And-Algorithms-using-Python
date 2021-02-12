
def binarySearch( theSequence, target, first, last ) :
    if first > last :
        return False

    else :
        mid = ( first + last ) // 2
        if theSequence[ mid ] == target :
            return True

        elif theSequence[ mid ] < target :
            return binarySearch( theSequence, target, mid + 1, last )

        else :
            return binarySearch( theSequence, target, first, mid - 1 )

seq = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
print( binarySearch( seq, 10, 0, len( seq ) ) )



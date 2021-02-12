list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Iterative version.
def printRev( theList ) :
    n = len( theList )
    i = n - 1

    while i >= 0 :
        print( theList[i] )
        i -= 1

printRev( list1 )

print()

# Recursive version.
def printRev1( theList ) :
    if len( theList ) > 0 :
        print( theList[ len(theList) - 1 ] )
        printRev1( theList[: len( theList ) - 1 ] )

printRev1( list1 )




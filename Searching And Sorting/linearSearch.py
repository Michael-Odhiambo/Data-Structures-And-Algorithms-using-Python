
def linearSearch( theList, item ) :
    n = len( theList )

    for i in range( n ) :
        if theList[i] == item :
            return True

    return False

myList = [1, 2, 3, 4, 5]
print( linearSearch( myList, 2 ) )
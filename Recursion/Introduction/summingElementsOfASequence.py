
def theSum( seq ) :
    if len( seq ) == 1 :
        return seq[0]

    return seq[0] + theSum( seq[1:] )

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print( theSum( myList ) )
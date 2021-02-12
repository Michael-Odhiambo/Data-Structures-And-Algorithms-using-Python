

def calOffset( row, col ) :
    rows = 15
    cols = 15

    offset = ( row * cols ) + col

    return offset

def findPosition( theList, row, col ) :

    targetOffset = calOffset( row, col )

    low = 0
    high = len( theList ) - 1

    while low <= high :
        mid = ( low + high ) // 2
        midOffset = calOffset( theList[ mid ].row, theList[ mid ].col ) 

        if midOffset == targetOffset :
            return mid

        elif midOffset < targetOffset :
            low = mid + 1

        else :
            high = mid - 1

    return low

class Element :
    def __init__( self, row, col ) :
        self.row = row
        self.col = col

def insertElement( theList, element, index ) :
    theList.insert( index, element)

myList = list()

element1 = Element( 0, 1 )
index = findPosition( myList, element1.row, element1.col )
insertElement( myList, element1, index )

element2 = Element( 1, 2 )
index = findPosition( myList, element2.row, element2.col )
insertElement( myList, element2, index )

element3 = Element( 0, 3 )
index = findPosition( myList, element3.row, element3.col )
insertElement( myList, element3, index )

element4 = Element( 0, 2 )
index = findPosition( myList, element4.row, element4.col )
insertElement( myList, element4, index )

element5 = Element( 0, 15 )
index = findPosition( myList, element5.row, element5.col )
insertElement( myList, element5, index )

for element in myList :
    item = element.row, element.col
    print( item )
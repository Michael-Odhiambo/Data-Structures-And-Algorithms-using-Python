# Given the following list of keys (80, 7, 24, 16, 43, 91, 35, 2, 19, 72), show the
# contents of the array after each iteration of the outer loop for the indicated
# algorithm when sorting in ascending order.

# (a) bubble sort (b) selection sort (c) insertion sort

myList = [ 80, 7, 24, 16, 43, 91, 35, 2, 19, 72 ]

def bubbleSort( theSeq ) :
    n = len( theSeq )
    for i in range( n - 1 ) :
        for j in range( n - 1 - i ) :
            if theSeq[j] > theSeq[j + 1] :
                theSeq[j], theSeq[j + 1] = theSeq[j + 1], theSeq[j]

        print( theSeq )

bubbleSort( myList )
print()
print( "-----------------------------------------" )

def selectionSort( theSeq ) :
    n = len( theSeq )

    for i in range( n ) :
        smallIndex = i
        for j in range( i + 1, n ) :
            if theSeq[j] < smallIndex :
                smallIndex = j

        if smallIndex != i :
            theSeq[i], theSeq[smallIndex] = theSeq[smallIndex], theSeq[i]

        print( theSeq)

selectionSort( myList )
print( "-------------------------------------------" )


def insertionSort( theSeq ) :
    n = len( theSeq )

    for i in range( 1, n ) :
        value = theSeq[i]
        pos = i

        while pos > 0 and value < theSeq[ pos - 1 ] :
            theSeq[ pos ] = theSeq[ pos - 1 ]
            pos -= 1

        theSeq[ pos ] = value
        print( theSeq )

insertionSort( myList )

print( "==========================================" )
list2 = [ 3, 18, 29, 32, 39, 44, 67, 75 ]
bubbleSort( list2 )
print( "===============================================" )
selectionSort( list2 )
print( "=============================================" )
insertionSort( list2 )


    


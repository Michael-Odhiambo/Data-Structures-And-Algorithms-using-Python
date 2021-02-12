
# Implementation of the bubble sort algorithm.
def bubbleSort( theValues ) :
    n = len( theValues ) - 1
    # Go through the values.
    for i in range( n ) :
        for j in range( n - i ) :
            if theValues[j] > theValues[j + 1] :
                theValues[j], theValues[j + 1] = theValues[j + 1], theValues[j]

    return theValues

myList = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
print( bubbleSort( myList ) )
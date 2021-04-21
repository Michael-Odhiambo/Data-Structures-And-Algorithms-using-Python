# Function to read the text file and store the words in it.
def readTheFile( theFile ) :
    with open( theFile ) as f :
        lines = f.readlines()

    f.close()

    return lines


# Implementation of the selection sort algorithm.
def selectionSort( theText ) :
    n = len( theText )

    # Find the smallest value's index.
    for i in range( n - 1 ) :
        # Assume the ith element is the smallest.
        smallIndex = i
        # Go through the unsorted part of the sequence.
        for j in range( i + 1, n ) :
            if theText[j] < theText[smallIndex] :
                smallIndex = j

        # Swap the ith value and smallNdx value only if the smallest value is
        # not already in its proper position. Some implementations omit testing
        # the condition and always swap the two values.
        if smallIndex != i :
            theText[i], theText[smallIndex] = theText[smallIndex], theText[i]

    return theText



# Store the sorted words in a list.
sortedFile = selectionSort( readTheFile( "20k.txt" ) )

# Write the results in a new file called "InsertionSorted20k.txt".
with open( "SelectionSorted20k.txt", 'w' ) as f :
    for i in range( len( sortedFile ) ) :
        f.write( sortedFile[i] )

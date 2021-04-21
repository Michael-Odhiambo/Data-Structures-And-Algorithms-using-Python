
# Function to read the text file and store the words in it.
def readTheFile( theFile ) :
    with open( theFile ) as f :
        lines = f.readlines()

    f.close()

    return lines

# Implementation of the insertion sort algorithm.
def insertionSort( theText ) :
    n = len( theText )

    # Start with the first word as the only
    # sorted word.
    for i in range( 1, n ) :
        # Save the value to be positioned.
        value = theText[i]
        # Find the position where the value fits in
        # the sorted part of the list.
        pos = i
        while pos > 0 and value < theText[ pos - 1 ] :
            theText[ pos ] = theText[ pos - 1 ]
            pos -= 1

        theText[pos] = value

    return theText

# Store the sorted words in a list.
sortedFile = insertionSort( readTheFile( "20k.txt" ) )

# Write the results in a new file called "InsertionSorted20k.txt".
with open("InsertionSorted20k.txt", 'w') as f :
    for i in range( len( sortedFile ) ) :
        f.write( sortedFile[i] )





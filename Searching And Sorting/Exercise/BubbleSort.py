
# Function to read the text file and store the words in it.
def readTheFile( theFile ) :
    with open( theFile ) as f :
        lines = f.readlines()

    f.close()

    return lines

# Sorts a sequence in ascending order using the bubble sort algorithm.
def bubbleSort( theText ) :
    n = len( theText )
    # Perform n-1 bubble operations on the sequence.
    for i in range( n - 1 ) :
        # Bubble the largest item to the end.
        for j in range( n - 1 - i ) :
            if theText[j] > theText[j + 1] : # Swap the j and j + 1 items.
                tmp = theText[j]
                theText[j] = theText[j + 1]
                theText[j + 1] = tmp

    return theText

# Store the sorted words in a list.
sortedFile = bubbleSort( readTheFile( "20k.txt" ) )

# Write the results in a new file called "InsertionSorted20k.txt".
with open( "BubbleSorted20k.txt", 'w' ) as f :
    for i in range( len( sortedFile ) ) :
        f.write( sortedFile[i] )

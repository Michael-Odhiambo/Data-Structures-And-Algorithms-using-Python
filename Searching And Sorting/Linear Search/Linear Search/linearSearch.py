

# Implementation of the linear search on an unsorted list.

def linearSearch( theValues, target ) :
    n = len( theValues )  

    # Go through the values.
    for i in range( n ) :
        # if the target is at the ith element, return True.
        if theValues[i] == target :
            return True

    return False   # Target not found.


# Implementation of the linear search on a sorted list.
def sortedLinearSearch( theValues, target ) :
    n = len( theValues )
    
    # Go through the values.
    for i in range( n ) :
        # If the target is at the ith value, return True.
        if theValues[i] == target :
            return True

        # If the ith element is greater than target element, it is not in the list.
        elif theValues[i] > target :
            return False

    return False


# Finding the smallest value in a collection.
def findSmallest( theValues ) :
    n = len( theValues )

    # We assume the first value is the smallest.
    smallest = theValues[0]

    for i in range( 1, n ) :
        # if the value at position i is less than smallest, put it as the smallest.
        if theValues[i] < smallest :
            smallest = theValues[i]

    return smallest     # Return the smallest found.

        
            


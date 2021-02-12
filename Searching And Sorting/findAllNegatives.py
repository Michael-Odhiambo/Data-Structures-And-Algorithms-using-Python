# Design and implement a function to find all negative values within a given list.
# Your function should return a new list containing the negative values. When
# does the worst case occur and what is the run time for that case?
def findAllNegatives( myList ) :
    newList = list()

    for val in myList :
        if val < 0 :
            newList.append( val )

    return newList

myList = [ -1, 2, -3, 2 ]
print( findAllNegatives( myList ) )

# Assuming the list is sorted, We can design a better implementation by allowing the loop to
# break early.
def findAllNegatives1( myList ) :
    newList = list()

    for val in myList :
        if val >= 0 :
            return newList
        else :
            newList.append( val )
    
    return newList


list2 = [-4, -3, -2, -1, 0, 1, 2 ]
print( findAllNegatives1( list2 ) )
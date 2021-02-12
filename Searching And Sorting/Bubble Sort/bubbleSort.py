
# Sorts a sequence in ascending order using the bubble sort algorithm.
def bubbleSort( theSeq ) :
    n = len( theSeq )
    # Perform n-1 bubble operations on the sequence.
    for i in range( n - 1 ) :
        # Bubble the largest item to the end.
        for j in range( n - 1 - i ) :
            if theSeq[j] > theSeq[j + 1] : # Swap the j and j + 1 items.
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp

    return theSeq



# The bubble sort algorithm can be improved by having it terminate early and not require it to perform all n ^ 2
# iterations when the sequence is in sorted order. We can determine the sequence is in sorted order when no
# swaps are performed by the if statement within the inner loop. At that point, the function can return 
# immediately without completing the remaining iterations. If a value is out of sorted order, then it will either
# be smaller than its predecessor in the sequence or larger than its successor at which point the condition of
# the if statement would be true. This improvement introduces a best case that only requires O(n) time when the
# input sequence is in sorted order.

def bubbleSort1( theSeq ) :
    n = len( theSeq )

    # Perform n - 1 bubble operations on the sequence.
    for i in range( n - 1 ) :
        # Bubble the largest item to the end.

        count = 0  # Keep track of the number of swaps.

        for j in range( n - 1 - i ) :
            if theSeq[j] > theSeq[j + 1] : # Swap the j and j + 1 items.
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
                
                count += 1  # If a swap occurs, count it.
       
        # If no swap occurs, meaning the sequence is sorted, break.
        if count == 0 :
            return theSeq

    return theSeq

































    


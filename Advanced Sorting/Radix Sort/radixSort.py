
from arrayADT import Array
from queue import Queue

def radixSort( intList, numDigits ) :
    # Create an array of queues to represent the bins.
    binArray = Array( 10 )
    for k in range( 10 ) :
        binArray[ k ] = Queue()

    # The value of the current column.
    column = 1  # Ones, tens, hundreds...

    # Iterate over the number of digits in the largest value.
    for d in range( numDigits ) :
        # Distribute the keys across the 10 bins.
        for key in intList :
            digit = ( key // column ) % 10
            binArray[ digit ].enqueue( key )

        # Gather the keys from the bins and place them back in intList.
        i = 0
        for bin in binArray :
            while not bin.isEmpty() :
                intList[i] = bin.dequeue()
                i += 1

        # Advance to the next column value.
        column *= 10

mySeq = [ 10, 23, 51, 18, 4, 31, 5, 13, 39, 38, 29, 39, 392, 3892, 37, 3892, 2983, 9283, 8329, 3928, 9283, 283, 8298, 9283, 9283, 838, 497, 489, 9384, 743, 9834, 53, 44, 645, 324, 564, 654, 567, 645, 54, 3, 64, 65, 545, 645, 656, 7675, 645, 6524, 634, 6243, 7545, 5776, 53, 54, 425, 4234, 657, 5686, 656, 6356654, 74, 54, 2, 34, 57,676, 567, 86, 56, 5443, 56, 4423, 65, 76, 9, 7565, 56, 453, 54, 54, 3432, 2, 1, 43, 6, 54, 5654, 5354, 5, 4234, 65, 453, 452, 142, 654, 53, 432, 45, 424, 366, 76, 5888866, 765, 98, 56345, 4523, 75, 45, 345, 56, 543, 234, 1,3212, 123, 654, 345, 54, 754, 434, 32454, 366, 434, 42, 313, 341, 645, 74, 56345, 523456547653, 42, 43143, 3123, 4345, 453, 634, 453, 4234, 4345, 65, 2, 87, 8765, 757, 4567, 645, 78, 967,8 ,765, 0, 86890, 764, 365, 254, 4524, 564, 74563, 24, 5245, 4234, 42345, 4235, 564,6 ,76456, 8974853 ,524, 7654 ]
radixSort( mySeq, 7 )
print( mySeq )

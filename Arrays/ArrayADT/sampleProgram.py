
# The following simple program illustrates the creation and use of an array object
# based on the Array ADT.

# Fill a 1-D array with random values then print each value, one per line.

from arrayADT import Array
import random

# The constructor is called to create the array.
valueList = Array( 100 )

# Fill the array with random floating-point values.
for i in range( len(valueList) ) :
    valueList[ i ] = random.random()

# Print the values one per line.
for value in valueList :
    print( value )

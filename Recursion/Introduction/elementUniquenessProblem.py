
"""
By Michael Odhiambo.
03/12/2020 ~ 19:11

"""

from time import time

def unique( lst ) :
    if len( lst ) == 1 :
        return True

    for n in lst[1:] :
        if n == lst[0] :
            return False
    return unique( lst[1:] )

def unique1( seq ) :
    for i in range( len( seq ) ) :
        for j in range( i + 1, len( seq ) ) :
            if seq[i] == seq[j] :
                return False
    return True

import sys
sys.setrecursionlimit( 10000 )

myList = list()
for i in range( 1000 ) :
    myList.append( i )

start = time()

for i in range( 1000 ) :
    unique( myList )

end = time()
print( ( end - start ) / i )

start = time()

for i in range( 1000 ) :
    unique1( myList )

end = time()
print( ( end - start ) / i )



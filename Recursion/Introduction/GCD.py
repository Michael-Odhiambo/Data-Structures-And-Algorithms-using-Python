
# Design and implement a recursive function for computing the greatest
# common divisor of two integer values.

# The greatest common divisor of two integers a and b, GCD( a, b ), not both of which are
# zero, is the largest positive integer that divides both a and b. The Euclidean algorithm
# for finding this greatest common divisor of a and b is as follows:

#     - Divide a by b to obtain the integer quotient q and remainder r, so that
#       1 = bq + r. ( if b = 0, GCD( a, b ) = a. ) Then GCD( a, b ) = GCD( b, r ).
#       Replace a with b and b with r, and repeat this procedure. Since the remainders
#       are decreasing, eventually a remainder of 0 will result. The last nonzero remainder
#       is GCD( a, b ).

# Note: If either a or b is negative, replace it with its absolute value.


def GCD( a, b ) :
    if b == 0 :
        return a

    r = a % b

    if r == 0 :
        return b

    return GCD( b, r )

print( GCD( 1260, 198 ) )

# The least common multiple of a and b, LCM( a, b ), is the smallest non-negative integer
# that is a multiple of both a and b and can be calculated using :

#       LCM( a, b ) = | a * b | // ( GCD( a, b ) )

def LCM( a, b ) :
    return abs( a * b ) // GCD( a, b )

print( LCM( 10, 20 ) )



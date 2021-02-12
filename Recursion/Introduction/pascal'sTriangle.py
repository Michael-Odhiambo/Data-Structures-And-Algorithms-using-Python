
# Design and implement a program that prints Pascal's Triangle using a recursive implementation
# of the binomial coefficients function.

#             a( n, r ) = n! //( n - r )!

def factorial( n ) :
    if n == 0 :
        return 1
    return n * factorial( n - 1 )


def binCoefficients( n, k ) :
    if k == 0 or k == n :
        return 1
    coeff = binCoefficients( n - 1, k - 1 ) + binCoefficients( n - 1, k )
    return coeff

for i in range( 6 ) :
    print( binCoefficients( 6, i ) , end = " " )


def comma( num ) :
    n = num[0]
    if len( num ) == 1 :
        return num

    elif len( num[1:] ) % 3 == 0 :
        n = n + "," + comma( num[1:] )
        return n
    else :
        return comma( num[1:] )

print( comma( "1000" ) )





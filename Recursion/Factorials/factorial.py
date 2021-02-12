
# Recursive version.
def factorial( n ) :
    # The base case.
    if n < 2 :
        return 1
    else :
        return n * factorial( n - 1 )

print( factorial(50) )

# Iterative version.
def factorial1( n ) :
    fac = 1

    for i in range( 1, n + 1 ) :
        fac *= i

    return fac

print( factorial1( 50 ) )


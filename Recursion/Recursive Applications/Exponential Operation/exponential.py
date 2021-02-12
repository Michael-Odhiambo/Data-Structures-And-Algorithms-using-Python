
# Iterative version.
def exp1( x, n ) :
    result = 1
    for i in range( n ) :
        result *= x

    return result

print( exp1( 2, 1000 ) )

# Recursive version.
def exp2( x, n ) :
    if n == 0 :
        return 1
    result = exp2( x * x, n // 2 )
    if n % 2 == 0 :
        return result
    else :
        return x * result

print( exp2( 2, 1000 ) )
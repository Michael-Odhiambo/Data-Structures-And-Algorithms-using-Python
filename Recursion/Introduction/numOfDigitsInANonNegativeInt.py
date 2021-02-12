
# Write a recursive function that returns the number of digits in a non-negative integer.

def numOfDigits( num ) :
    count = 1
    if len( num ) == 1 :
        return count
    count += numOfDigits( num[1:] )
    return count

num = "1983787589328378593948090189375938028349018394789"
print( len( num ) )
print( numOfDigits( num ) )
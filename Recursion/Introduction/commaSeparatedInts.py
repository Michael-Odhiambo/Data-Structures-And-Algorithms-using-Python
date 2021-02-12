
# By Michael Odhiambo.
# Date 03/12/2020

# Write a recursive procedure that displays a non-negative integer with
# commas in the correct locations.

def comma( num ) :
    n = num[0]
    if len( num ) == 1 :
        return n

    elif len( num[1:] ) % 3 == 0 :
        n = n + "," + comma( num[1:] )
        return n
    else :
        return n + comma( num[1:] )

print( comma( "50000" ) )
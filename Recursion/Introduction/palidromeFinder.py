
# Design and implement a recursive function for determining whether a string
# is a palidrome. A palidrome is a string of characters that is the same as
# the string of characters in reverse.

def palidrome( str ) :
    if len( str ) == 1 :
        return True

    elif str[0] == str[-1] :
        return palidrome( str[1:-1] )
    else :
        return False

print( palidrome( "racecar" ) )
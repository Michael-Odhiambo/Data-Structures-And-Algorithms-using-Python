
"""
By Michael Odhiambo.
03/12/2020  ~ 17:47

"""
def printRuler( n ) :
    if n >= 1 :
        printRuler( n - 1 )
        print( " - " * n )
        printRuler( n - 1 )

print( " - " * 5 )
printRuler( 4 )
print( " - " * 5 )
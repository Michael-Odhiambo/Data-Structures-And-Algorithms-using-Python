
def fibonacci( n ) :
    n1 = 1
    n2 = 1
    nth = 0

    print( n1 )
    print( n2 )
    
    i = 2

    while i < n :
        nth = n1 + n2

        print( nth )
        n1 = n2
        n2 = nth

        i += 1

fibonacci( 10 )

for i in range( -1, 2 ) :
    print( i )


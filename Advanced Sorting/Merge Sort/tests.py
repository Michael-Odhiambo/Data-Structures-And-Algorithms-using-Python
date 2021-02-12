

def mul( n ) :
    if n >= 1 :
        mul( n - 1)
        for i in range( 1, n + 1 ) :
            print( n * i, end = " " )
        print()

#mul( 9 )

for i in range( 1, 10 ) :
    print( end = " ")
    print( i, end = " " )
print()

for i in range( 1, 10 ) :
    print( i, end = " " )
    for j in range( 1, i + 1 ) :
        print( i * j, end = " " )
    print()



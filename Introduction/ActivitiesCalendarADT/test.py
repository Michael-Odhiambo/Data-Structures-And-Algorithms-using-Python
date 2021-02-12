
one = 1
two = 2
three = 3
four = 4

if ( one == 2 ) and ( two == 2 and three == 3 and four == 4 ) :
    print( "Yes" )
else :
    print( "No" )


myDates = { "BasketBall Finals" : 'Date' }

values = [ myDates.values() ]


for value in values :
    if value == 'Date' :
        print(myDates[value].key() )
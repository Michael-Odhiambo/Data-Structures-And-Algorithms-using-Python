

month = 13

if len( str( month ) ) > 2 or ( month < 1 or month > 12 ) :
    print( "Failed" )
else :
    print( "Passed" )

year = 1

if not type( year ) == int :
    print( "Failed" )
else :
    print( "Passed" )

month = [ ("January", 31) ]
print( month[0][1] )

myList = [ None , "Mike", "Allan" ]
for name in myList :
    print( name )

monthNames = [ ( "January", 31 ), ( "February", 28 ), ( "March", 31 ), ( "April", 30 ), \
            ( "May", 30 ), ( "June", 30 ), ( "July", 31 ), ( "August", 31 ),\
                 ( "September", 30 ), ( "October", 31 ), ( "November", 30 ), ( "December", 31 ) ]

for month in monthNames :
    print( month[0] )

date1 = 2
date2 = None

if not date1 or not date2 :
    print( "Current Date." )
else :
    print( "Given Date" )

import datetime
myDate = datetime.date.today()
print( myDate.day )
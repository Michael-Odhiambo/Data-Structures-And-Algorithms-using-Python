
from linearbag import Bag
from dateADT import Date

def main() :
    bornBefore = Date( 7, 16, 1999 )
    bag = Bag()

    # Extract dates from the user and place them in the bag.
    date = promptAndExtractDate()

    while date is not None :
        bag.add( date )
        date = promptAndExtractDate()

    # Iterate over the bag and check the age.
    for date in bag :
        if date <= bornBefore :
            print( "Is at least 21 years of age: ", date )
        else :
            print( "Sorry, this one is underage: ", date )

def promptAndExtractDate() :
    print( "Enter a birth date." )
    month = int(input( "Enter the month (0 to quit): " ))
    
    if month == 0 :
        return None
    else :
        day = int( input("Enter day: ") )
        year = int( input("Enter year: ") )

    return Date( month, day, year )

# Call the main routine.
main()      

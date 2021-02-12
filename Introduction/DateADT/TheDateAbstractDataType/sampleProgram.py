
"""
To illustrate the use of the Date ADT, consider the program below, which processes a collection of birth dates.
The dates are extracted from standard input and examined. Those dates that indicate the individual is at least
21 years of age based on a target date are printed to standard output. The user is continuously prompted to 
enter a birth date until zero is entered for the month.

This simple example illustrates an advantage of working with an abstraction by focusing on what fuctionality
the ADT provides instead of how that functionality is implemented. By hiding the implementation details, we
can use an ADT independent of its implementation. In fact, the choice of implementation for the Date ADT will
have no effect on the instructions in our example program.

"""

from dateADT import Date

def main() :
    # Date before which a person must have been born to be 21 or older.
    bornBefore = Date( 7, 16, 1999 )

    # Extract birth dates from the user and determine if the individual is 21 or older.
    date = promptAndExtractDate()
    
    while date is not None :
        if date <= bornBefore :
            print( "Is atleast 21 years of age: ", date )
        else :
            print( "Sorry" )
 
        date = promptAndExtractDate()

# Prompts for and extracts the Gregorian date components. Returns a Date object or None when the user has
# finished entering dates.
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
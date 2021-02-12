
# Implementing The ADT.

# For our implementation, we will store the date as an integer value representing the Julian day, which is the
# number of days elapsed since the initial date of November 24, 4713 BC ( using the Gregorian calendar notation
# ). Given a julian day number, we can compute any of the three Gregorian components and simply subtract the
# tow integer values to determine which occurs first or how many days separate the two dates. 

# Implementes a proleptic Gregorian calendar date as a Julian day number.

import calendar
import datetime

class Date :

    # Creates an object instance for the specified Gregorian date.
    def __init__( self, month = None, day = None, year = None ) :

        # If any of the arguments is not given in the constructor, initialize the date
        # to the current date.
        if not month or not day or not year :
            today = datetime.date.today()
            month, day, year = today.month, today.day, today.year
            
        self._julianDay = 0
        assert self._isValidGregorian( month, day, year ), \
            "Invalid Gregorian date."

        # The first line of the equation, T = (M - 14) / 12, has to be changed since Python's
        # implementation of integer division is not the same as the mathematical definition.
        tmp = 0
        if month < 3 :
            tmp = -1
        self._julianDay = day - 32075 + \
            (1461 * (year + 4800 + tmp) // 4) + \
                (367 * (month - 2 - tmp * 12) // 12) - \
                    (3 * ((year + 4900 + tmp) // 100) // 4)

    # Returns the Gregorian date as a tuple: (month, day, year).
    def _toGregorian( self ) :
        A = self._julianDay + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A // 2447
        day = A - (2447 * month // 80)
        A = month // 11
        month = month + 2 - (12 * A)
        year = 100 * (B - 49) + year + A
        
        return month, day, year

    # Verifies that the given date is valid.
    def _isValidGregorian( self, month, day, year ) :
        isValid = True

        # The month must have a maximum of two digits in the range of 1..12.
        if len( str(month) ) > 2 or ( month < 1 or month > 12 ) :
            isValid = False

        # The day must have a maximum of two digits in the range of 1...31.
        if len( str(day) ) > 2 or ( day < 1 or day > 31 ) :
            isValid = False

        # The year can be any positive or negative integer value.
        if not type( year ) == int :
            isValid = False

        return isValid


    # Extracts the appropriate Gregorian date component.
    def month( self ) :
        return ( self._toGregorian() )[0]

    def day( self ) :
        return ( self._toGregorian() )[1]
    
    def year( self ) :
        return ( self._toGregorian() )[2]

    # Returns the day of the week as an int between 0 ( Mon ) and 6 ( Sun ).
    def dayOfWeek( self ) :
        month, day, year = self._toGregorian()
        if month < 3 :
            month = month + 12
            year = year - 1
        
        return ((13 * month + 3) // 5 + day + \
            year + year // 4 - year // 100 + year // 400 ) % 7

    def _months( self ) :
        monthNames = [ ( "January", 31 ), ( "February", 28 ), ( "March", 31 ), ( "April", 30 ), \
            ( "May", 30 ), ( "June", 30 ), ( "July", 31 ), ( "August", 31 ),\
                 ( "September", 30 ), ( "October", 31 ), ( "November", 30 ), ( "December", 31 ) ]

        return monthNames


    # Returns the month name of the given date.
    def monthName( self ) :
        return self._months()[ self.month() - 1 ][0]


    # Determines if the given date falls in a leap year.
    # 1.) If a year is evenly divisible by 4, go to the next step. If it's not, then it's 
    #     not a leap year.
    # 2.) If a year is divisible by 4, but not by 100, it is a leap year. If a year is divisible
    #     by both 4 and 100, go to the next step.
    # 3.) If a year is divisible by 100, but not by 400, then it's not a leap year. If a year is 
    #    divisible by both, then it's a leap year.
    def isLeapYear( self ) :
        if self.year() % 4 == 0 :
            if self.year() % 100 == 0 :
                if self.year() % 400 == 0 :
                    return True

                else :
                    return False

            else :
                return True

        else :
            return False

    # Returns the number of days in the month of the given date.
    def numDays( self ) :
        if self.month() == 2 :
            if self.isLeapYear() :
                return 29

        return self._months()[ self.month() ][1]

    # Advances the date by the given number of days.
    def advanceBy( self, numDays ) :
        self._julianDay += numDays
        month, day, year = self._toGregorian()

        return Date( month, day, year )

    def _daysOfTheWeek( self ) :
        weekDays = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",\
            "Saturday", "Sunday" ]

        return weekDays

    # Returns an integer indicating the day of the year.
    def dayOfYear( self ) :
        count = 0
        for month in self._months() :
            if month[0] == self.monthName() :
                count += self._toGregorian()[1]
                break

            else :
                count += month[1]

        return count


    # Returns a string containing the name of the day.
    def dayOfWeekName( self ) :
        return self._daysOfTheWeek()[ self.dayOfWeek() ]

    # Determines if the date is a weekday.
    def isWeekDay( self ) :
        if self.dayOfWeek() < 5 :
            return True

        return False

    # Determines if the date is the spring or autumn equinox.
    # ( March 19 and September 22 ).
    def isEquinox( self ) :
        if self.monthName() == "March" :
            if self.day() == 19 :
                return True

        if self.monthName() == "September" :
            if self.day() == 22 :
                return True

        return False


    # Determines ( June 21 or 22 ).
    def isSoltice( self ) :
        if self.monthName() == "June" :
            if self.day() == 21 or self.day() == 22 :
                return True

        return False

    
    # Similar to the __str__() method but uses the optional argument "divchar" as the dividing
    # character between the three components of the Gregorian date.
    def asGregorian( self, divchar = '/' ) :
        month, day, year = self._toGregorian()
        return "%02d%s%02d%s%04d" % ( month, divchar, day, divchar, year ) 

    # Accepts a date object and prints a calendar for the month of the given date. 
    def printCalendar( self ) :
        return calendar.month( self.year(), self.month() )

    # Returns the date as a string in Gregorian format.
    def __str__( self ) :
        month, day, year = self._toGregorian()
        return "%02d/%02d/%04d" % ( month, day, year )

    # Logically compares the two dates.
    def __eq__( self, otherDate ) :
        return self._julianDay == otherDate._julianDay

    def __lt__( self, otherDate ) :
        return self._julianDay < otherDate._julianDay

    def __le__( self, otherDate ) :
        return self._julianDay <= otherDate._julianDay

myDate = Date( 2, 1, 2000 )
print( myDate )
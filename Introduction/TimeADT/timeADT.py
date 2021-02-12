

class Time :

    def __init__( self, hours, minutes, seconds ) :

        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

        self._secsAfterMidnight = 0

        self._secsAfterMidnight = ( hours * 3600 ) + ( minutes * 60 ) + seconds

    # Returns the hour part of the time.
    def hours( self ) :
        return self._hours

    # Returns the minutes part of the time.
    def minutes( self ) :
        return self._minutes

    # Returns the seconds part of the time.
    def seconds( self ) :
        return self._seconds

    # Returns the number of seconds as a positive integer between this time and otherTime.
    def numSeconds( self, otherTime ) :
        return abs( self._secsAfterMidnight - otherTime._secsAfterMidnight )

    # Determines if this time is ante meridien or before midday ( at or before 12 o'clock noon ).
    def isAM( self ) :
        secsToMidnight = 43200
        if self._secsAfterMidnight < secsToMidnight :
            return True

        return False

    # Determines if this time is post meridiem or after midday( after 12 o'clock noon ).
    def isPM( self ) :
        if not self.isAM() :
            return True

        return False

    # Compares if this time is to otherTime to determine their logical ordering. This comparison can be
    # done using any of the Python logical operators.
    def __lt__( self, otherTime ) :
        return self._secsAfterMidnight < otherTime._secsAfterMidnight

    def __le__( self, otherTime ) :
        return self._secsAfterMidnight <= otherTime._secsAfterMidnight

    def __eq__( self, otherTime ) :
        return self._secsAfterMidnight == otherTime._secsAfterMidnight

    # Returns a string representing the time in the 12-hour format hh:mm:ss. Invoked by calling
    # Python's str() constructor.
    def __str__( self ) :
        return "%02d:%02d:%02d" % ( self.hours(), self.minutes(), self.seconds() )


myTime = Time( 1, 30, 0 )
print( myTime )


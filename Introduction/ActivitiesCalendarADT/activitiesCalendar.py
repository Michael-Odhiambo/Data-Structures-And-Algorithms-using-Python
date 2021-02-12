
from DateADT import Date
import calendar

class ActivitiesCalendar :

    def __init__( self, dateFrom, dateTo ) :

        self._dateFrom = dateFrom
        self._dateTo = dateTo
        assert ( self._dateFrom < self._dateTo ) and ( self._dateTo.month() <= self._dateFrom.month() and self._dateTo.day() <= self._dateFrom.day() ),\
            "Invalid range for the calendar."

        # A list to store the activities in the calendar.
        self._activities = list()

    # Returns the number of activities on the calendar.
    def length( self ) :
        return len( self._activities )

    # Returns the string that describes the activity for the given date if an activity exists
    # for the given date; otherwise, None is returned.
    def getActivity( self, date ) :
        for value in self._activities :
            if value[0] == date :
                return value[1]

        return None
        
    # Adds the given activity description to the calendar for the given date. The date must be within the
    # valid range for the calendar.
    def addActivity( self, date, activity ) :
        assert date >= self._dateFrom and date <= self._dateTo, "Invalid date range."
        theActivity = date, activity
        self._activities.append( theActivity )

    # Displays to standard output all activities for the given month. The display includes the year and 
    # name of the month and the list of activities for the month. The display of each activity includes
    # the day of the month on which the activity occurs and the description of the activity.
    def displayMonth( self, month ) :

        theActivities = list()

        for activity in self._activities :
            if activity[0].month() == month :
                theActivities.append( activity )

        for activity in theActivities :
            print( activity[0].monthName(), str( activity[0] ), activity[1] )




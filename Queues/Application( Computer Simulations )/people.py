
# First, we need a class to store information related to a single passenger. We create
# a Passenger class for this purpose. The class will contain two data fields. The first
# is an identification number used in the output of the event information. The second
# field records the time the passenger arrives. This value will be needed to determine
# the length of time the passenger waited in line before beginning service with an agent.

class Passenger :
    def __init__( self, idNum, arrivalTime ) :
        self._idNum = idNum
        self._arrivalTime = arrivalTime

    # Get the passenger's id number.
    def idNum( self ) :
        return self._idNum

    # Gets the passenger's arrival time.
    def arrivalTime( self ) :
        return self._arrivalTime

# We also need a class to represent and store information related to the ticket agents.
# The information includes an agent identification number and a timer to know
# when the transaction will be completed. This value is the sum of the current time
# and the average time of the transaction as entered by the user. Finally, we need to
# keep track of the current passenger being served by the agent in order to identify
# the specific passenger when the transaction is completed.
# The passenger field is set to a null reference, which will be used to flag a
# free agent. The idNum() method simply returns the id assigned to the agent when
# the object is created while the isFree() method examines the passenger field to
# determine if the agent is free. The isFinished() method is used to determine if the
# passenger currently being served by this agent has completed her transaction. This
# method only flags the transaction as having been completed. To actually end the
# transaction, stopService() must be called. stopService() sets the passenger
# field to None to again indicate the agent is free and returns the passenger object.
# To begin a transaction, startService() is called, which assigns the appropriate
# fields with the supplied arguments.

class TicketAgent :

    def __init__( self, idNum ) :
        self._idNum = idNum
        self._passenger = None
        self._stopTime = -1

    # Gets the ticket agent's id number.
    def idNum( self ) :
        return self._idNum

    # Determines if the ticket agent is free to assist a passenger.
    def isFree( self ) :
        return self._passenger is None

    # Detemines if the agent has finished serving the passenger.
    def isFinished( self, curTime ) :
        return self._passenger is not None and self._stopTime == curTime

    # Indicates the agent has begun assisting a passenger.
    def startService( self, passenger, stopTime ) :
        self._passenger = passenger
        self._stopTime = stopTime

    # Indicates the agent has finished helping the passenger.
    def stopService( self ) :
        thePassenger = self._passenger
        self._passenger = None
        return thePassenger

    


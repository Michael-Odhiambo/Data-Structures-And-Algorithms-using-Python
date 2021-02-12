
# Finally, We construct the TicketCounterSimulation class to manage the actual simulation. This class
# will contain the various components, methods and data values required to perform a discrete event
# simulation. The first step in the constructor is to initialize three simulation parameters. Note the
# _arriveProb is the probability of a passenger arriving during the current time step using the formula
# described earlier. A queue is created, which will be used to represent the line in which the passengers
# must wait until they are served by a ticket agent. The Ticket agents are represented as an array of Agent
# objects. The individual objects are instantiated and each is assigned an id number, starting with 1.
# Two data fields are needed to store data collected during the actual simulation. The first is the
# summation of the time each passenger has to wait in line before being served, and the second keeps
# track of the number of passengers in the simulation. The latter will also be used to assign an id to
# each passenger.

# The simulation is performed by calling the run() method, which simulates the ticking of the clock by
# performing a count-controlled loop keeping track of the current time in curTime. The loop executes until
# _numMinutes have elapsed. The events of the simulation are also performed during the terminating minute,
# hence, the need for the _numMinutes + 1 in the range() function. During each iteration of the loop, the
# three simulation rules outlined earlier are handled by the respective handler methods. The _handleArrival()
# method determines if a passenger arrives during the current time step and handles that arrival.
# _handleBeginService() determines if any agents are free and allows the next passenger(s) in line to begin
# their transaction. The _handleEndService() determines which of the current transactions have completed, if
# any, and flags a passenger departure.

# After running the simulation, the printResults() method is called to print the results. When the simulation
# terminates there may be some passengers remaining in the queue who have not yet been assisted. Thus, we need
# to determine how many passengers have exited the queue, which indicates the number of passenger wait times
# included in the _totalWaitTime field. The average wait time is simply the total wait time divided by the number
# of passengers served.

from arrayADT import Array
from lListQueue import Queue
from people import Passenger, TicketAgent
import random


class TicketCounterSimulation :
    def __init__( self, numAgents, numMinutes, betweenTime, serviceTime ) :
        # Parameters supplied by the user.
        self._arrivalProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes

        # Simulation components.
        self._passengerQ = Queue()
        self._theAgents = Array( numAgents )

        for i in range( numAgents ) :
            self._theAgents[i] = TicketAgent(i + i)

        # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0

    # Run the simulation using the parameters supplied earlier.
    def run( self ) :
        for curTime in range( self._numMinutes + 1 ) :
            self._handleArrival( curTime )
            self._handleBeginService( curTime )
            self._handleEndService( curTime )

    # Print the simulation results.
    def printResults( self ) :
        numServed = self._numPassengers - len( self._passengerQ )
        avgWaitTime = float( self._totalWaitTime ) / numServed

        print("")
        print("Number of passengers served = ", numServed)
        print("Number of passengers remaining in line = %d" % len( self._passengerQ ) )
        print("The average wait time was %4.2f minutes." % avgWaitTime)

    # If a customer arrives, he is added to the queue. At most, one customer can arrive during
    # each time step.
    def _handleArrival( self, time ) :
        prob = random.random()

        if prob >= 0.0 and prob <= self._arrivalProb :
            self._numPassengers += 1
            passenger = Passenger( self._numPassengers, time )
            self._passengerQ.enqueue( passenger )
            print( "Passenger %d arrived." % ( self._numPassengers ) )

    # If there are customers waiting, for each free server the next customer in line begins
    # his/her transaction.
    def _handleBeginService( self, curTime ) :

        for agent in self._theAgents :
            if agent.isFree() and not self._passengerQ.isEmpty() :
                passenger = self._passengerQ.dequeue()
                stopTime = curTime + self._serviceTime

                waitTime = curTime - passenger.arrivalTime()
                self._totalWaitTime += waitTime
                agent.startService( passenger, stopTime )
                print( "Agent %d starts serving passenger %d " % ( agent.idNum(), passenger.idNum() ) )


    # For each server handling a transaction, if the transaction is complete, the customer
    # departs and the server becomes free.
    def _handleEndService( self, curTime ) :
        for agent in self._theAgents :
            if agent.isFinished( curTime ) :
                passenger = agent.stopService()

                agent.stopService()

                print( "Agent %d stopped serving passenger %d " % ( agent.idNum(), passenger.idNum() ) )








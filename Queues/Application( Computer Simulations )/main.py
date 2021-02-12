
from Simulation import TicketCounterSimulation
def main() :
    numMinutes = int( input( "Number of minutes to simulate: " ) )
    numAgents = int( input( "Number of ticket agents: " ) )
    serviceTime = int( input( "Average service time per passenger: " ) )
    betweenTime = int( input( "Average time between customer arrival: " ) )

    mySimulator = TicketCounterSimulation( numAgents, numMinutes, betweenTime, serviceTime )
    mySimulator.run()
    mySimulator.printResults()

main()



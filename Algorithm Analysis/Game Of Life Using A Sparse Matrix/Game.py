

# Program for playing game of Life.

from life import LifeGrid 

# Define the initial configuration of live cells.
coordinateList = [ (0, 0), (0, 4), (1, 1), (1, 3), (2, 2), (3, 1), (3, 3), (4, 0), (4, 4) ]

# Indicate the number of generations.
NUM_GENS = 8

def main() :
    # Construct the game grid and configure it.
    grid = LifeGrid()
    grid.configure( coordinateList )

    # Play the game.
    draw( grid )
    for i in range( NUM_GENS ) :
        evolve( grid )
        draw( grid )

# Generates the next generation of organisms.
def evolve( grid ) :

    minRow = grid.minRange()[0] 
    minCol = grid.minRange()[1] 
    maxRow = grid.maxRange()[0]
    maxCol = grid.maxRange()[1] 

    # List for storing the live cells of the next generation.
    liveCells = list()

    for row in range( minRow, maxRow + 1 ) :
        for col in range( minCol, maxCol + 1 ) :
            
            # Determine the number of live neighbors for this cell.
            neighbors = grid.numLiveNeighbors( row, col )

            # Add the ( i, j ) tuple to liveCells if this cell contains a live organism
            # in the next generation.
            if ( neighbors == 2 and grid.isLiveCell( row, col ) ) or \
                ( neighbors == 3 ) :
                liveCells.append( ( row, col ) )
                

    # Reconfigure the grid using the liveCells coord list.
    grid.configure( liveCells )

# Prints a text-based representation of the game grid.
def draw( grid ) :

    minRow = grid.minRange()[0]
    minCol = grid.minRange()[1]
    maxRow = grid.maxRange()[0]
    maxCol = grid.maxRange()[1] 

    print()

    print( "-----------------------------------------" )
    for row in range( minRow, maxRow + 1 ) :
        for col in range( minCol, maxCol + 1 ) :
            if grid.isLiveCell( row, col ) :

                print( " @ ", end = "" )

            else :
                print( " __ ", end = "" )
 
        print() 


# Executes the main routine.
main()

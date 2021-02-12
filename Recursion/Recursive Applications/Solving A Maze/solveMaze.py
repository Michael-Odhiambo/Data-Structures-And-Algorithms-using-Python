# Program for building and solving a maze.
from myMaze import Maze


# The main routine.
def main():
    maze = buildMaze("C:\\Users\\user\\Desktop\\myMaze.txt")
    if maze.findPath( maze.getStartPos() ) :
        print("Path found..")

    else:
        print("Path not found..")


# Builds a maze based on a text format in the given file.
def buildMaze( filename ):
    infile = open(filename, "r")

    # Read the size of the maze.
    nrows, ncols = readValuePair(infile)
    maze = Maze(nrows, ncols)
    print(maze.numRows(), maze.numCols())

    # Read the starting and exit positions.
    row, col = readValuePair(infile)
    maze.setStart(row, col)
    row, col = readValuePair(infile)
    maze.setExit( row, col )
    print( maze._startCell.row, maze._startCell.col )
    print(maze._exitCell.row, maze._exitCell.col)


    # Read the maze itself.
    for row in range(nrows):
        line = infile.readline()
        for col in range(len(line)):
            if line[col] == '*':
                maze.setWall(row, col)

    # Close the maze file and return the newly constructed maze.
    infile.close()
    return maze


# Extracts an integer value pair from the given input file.
def readValuePair(infile):
    line = infile.readline()
    valA, valB = line.split()
    return int(valA), int(valB)


# call the main routine to execute the program.
main()

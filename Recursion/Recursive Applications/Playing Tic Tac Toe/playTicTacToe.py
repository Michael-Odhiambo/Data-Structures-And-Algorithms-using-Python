
from board import Board, Player



availableTokens = [ "X", "O" ]
print( "Available Tokens: " )
for token in availableTokens :
    print( token, end = "  " )

print()



def main() :
    myBoard = Board()
    myBoard.draw()
    humanPlayer = input( "Pick your token: " ).upper()
    while humanPlayer not in availableTokens :
        print( "Please enter a valid token." )
        humanPlayer = input( "Pick your token: " ).upper()

    human = Player( humanPlayer )
    computer = Player( "O" ) if humanPlayer != "O" else Player( "X" )

    while myBoard.availableMoves() :
        humanMove = int( input( "Enter your move: " ) )
        while not myBoard.isValidMove( humanMove ) :
            print( "Please enter a valid move." )
            humanMove = int( input( "Enter your move: " ) )

        myBoard.makeMove( human.getToken(), humanMove )
        myBoard.draw()

        if myBoard.isWinner( human.getToken(), humanMove ) :
            print( "{} wins!!!".format( human.getToken() ) )
            break

        if myBoard.availableMoves() :
            computerMove = myBoard.findBestMove( computer.getToken() )
            myBoard.makeMove( computer.getToken(), computerMove )
            myBoard.draw()

            if myBoard.isWinner(computer.getToken(), computerMove) :
                print("{} wins!!!".format(computer.getToken()))
                break


main()

replay = input( "Do you want to play again ( Y or N ): " ).upper()

while not replay == "N" :
    main()
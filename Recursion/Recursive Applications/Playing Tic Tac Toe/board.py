from array2D import Array2D
import math

class Board :
    def __init__( self ) :
        self._theBoard = Array2D(3, 3)
        self._moves = list()
        self._markBoard()
        self.currentWinner = None
        self.count = 0

    def isValidMove( self, index ) :
        for move in self._moves :
            if move.getIndex() == index :
                row, col = move.getRowAndCol()
                if type( self._theBoard[row, col] ) == int :
                    return True

        return False

    def _markBoard( self ) :
        print()

        index = 0
        for row in range( self._theBoard.numRows() ) :
            for col in range( self._theBoard.numCols() ) :
                position = _Move( row, col, index )
                self._theBoard[ row, col ] = index
                self._moves.append( position )
                index += 1

    def draw( self ) :
        for row in range( self._theBoard.numRows() ) :
            for col in range( self._theBoard.numCols() ) :
                print( "|" + "{}".format( self._theBoard[row, col] ) + "|" , end = "" )
            print()

    def availableMoves( self ) :
        for row in range( self._theBoard.numRows() ) :
            for col in range( self._theBoard.numCols() ) :
                if type( self._theBoard[row, col] ) is int :
                    return True

        return False

    def makeMove( self, playerToken, position ) :

        for move in self._moves :
            if move.theIndex == position :
                row, col = move.getRowAndCol()

        if type( self._theBoard[row, col] ) is int :
            self._theBoard[row, col] = playerToken

            if self.isWinner( playerToken, position ) :
                self.currentWinner = playerToken
                return True

        return False

    def _checkRow( self, playerToken, position ) :
        rowIndex = math.floor( position / 3 )
        for col in range( 3 ) :
            if not self._theBoard[rowIndex, col ] == playerToken :
                return False

        return True

    def _checkCol( self, playerToken, position ) :
        colIndex = position % 3
        for row in range( 3 ) :
            if not self._theBoard[row, colIndex ] == playerToken :
                return False

        return True

    def _checkDiag1( self, playerToken, position ) :
        diagonal = [0, 4, 8]
        for ind in diagonal :
            for move in self._moves :
                if move.getIndex() == ind :
                    row, col = move.getRowAndCol()
                    if not self._theBoard[row, col] == playerToken :
                        return False

        return True

    def _checkDiag2(self, playerToken, position):
        diagonal = [2, 4, 6]
        for ind in diagonal:
            for move in self._moves:
                if move.getIndex() == ind:
                    row, col = move.getRowAndCol()
                    if not self._theBoard[row, col] == playerToken:
                        return False

        return True


    def isWinner( self, playerToken, position ) :
        if self._checkRow( playerToken, position ) :
            return True

        elif self._checkCol( playerToken, position ) :
            return True

        elif self._checkDiag1( playerToken, position ) :
            return True

        elif self._checkDiag2( playerToken, position ) :
            return True

        return False

    def _miniMax( self, playerToken, isMaximizing = True ) :
        computer = playerToken
        human = "X" if computer != "X" else  "O"
        self.count += 1
        print( self.count )

        if self.currentWinner == computer :
            return 1
        elif self.currentWinner == human :
            return -1

        if not self.availableMoves() :
            return 0

        if isMaximizing :
            bestScore = -math.inf
            for move in self._moves :
                row, col = move.getRowAndCol()
                if type( self._theBoard[row, col] ) == int :
                    self.makeMove( computer, move.getIndex() )
                    score = self._miniMax( playerToken, False )
                    self._theBoard[row, col] = move.getIndex()
                    self.currentWinner = None

                    bestScore = max( score, bestScore )

            return bestScore

        else :
            bestScore = math.inf
            for move in self._moves :
                row, col = move.getRowAndCol()
                if type( self._theBoard[row, col] ) == int :
                    self.makeMove( human, move.getIndex() )
                    score = self._miniMax( playerToken, True )
                    self._theBoard[row, col] = move.getIndex()
                    self.currentWinner = None

                    bestScore = min( score, bestScore )

            return bestScore





    def findBestMove( self, playerToken ) :

        bestScore = -math.inf
        bestMove = None

        for move in self._moves :
            row, col = move.getRowAndCol()
            if type( self._theBoard[ row, col ] ) is int :
                self.makeMove( playerToken, move.getIndex() )
                score = self._miniMax( playerToken, False )
                self._theBoard[row, col] = move.getIndex()
                if score > bestScore :
                    bestScore = score
                    bestMove = move.getIndex()

        return bestMove



class _Move :
    def __init__( self, row, col, index ) :
        self.theRow = row
        self.theCol = col
        self.theIndex = index

    def getRowAndCol( self ) :
        return self.theRow, self.theCol

    def getIndex( self ) :
        return self.theIndex

class Player :
    def __init__( self, token ) :
        self.token = token

    def getToken( self ) :
        return self.token





"""
myBoard = Board()
myBoard.draw()

player1 = "X"
player2 = "O"
while myBoard.availableMoves() :
    move = int( input( "Enter your move: " ) )
    myBoard.makeMove( player1, move )
    myBoard.draw()

    compMove = myBoard.findBestMove( player2 )
    myBoard.makeMove( player2, compMove )
    myBoard.draw()
"""


class EditBuffer :
    # Constructs an edit buffer containing one empty line of text.
    def __init__( self ) :
        self._firstLine = _EditBufferNode( ["\n"] )
        self._lastLine = self._firstLine
        self._curLine = self._firstLine
        self._curRowIndex = 0
        self._curColIndex = 0
        self._numLines = 1
        self._insertMode = True

    # Returns the number of lines in the buffer.
    def numLines( self ) :
        return self._numLines

    # Returns the number of characters in the current line.
    def numChars( self ) :
        return len( self._curLine.text )

    # Returns the index of the current row.
    def lineIndex( self ) :
        return self._curRowIndex

    # Returns the index of the current column (first col has index 0).
    def columnIndex( self ) :
        return self._curColIndex

    # Sets the entry mode based on the boolean value insert.
    def setEntryMode( self, insert ) :
        self._insertMode = insert

    # Toggles the entry mode between insert and overwrite.
    def toggleEntryMode( self ) :
        self._insertMode = not self._insertMode

    # Returns true if the current entry mode is insert.
    def inInsertMode( self ) :
        self._insertMode == True

    # Returns the character at the current cursor position.
    def getChar( self ) :
        return self._curLine.text[ self._curColIndex ]

    # Returns the current line as a string.
    def getLine( self ) :
        lineStr = ""
        for char in self._curLine.text :
            lineStr += char
        return lineStr

    # Moves the cursor up num lines.
    def moveUp( self, nLines ) :
        if nLines <= 0 :
            return

        elif self._curLinendex - nLines < 0 :
            nLines = self._curLineIndex

        for i in range( nLines ) :
            self._curLine = self._curLine.prev

        self._curLineIndex -= nLines
        if self._curColIndex >= self.numChars() :
            self.moveLineEnd()

    # Moves the cursor left one position.
    def moveLeft( self ) :
        if self._curColIndex == 0 :
            if self._curRowIndex > 0 :
                self.moveUp(1)
                self.moveLineEnd()
            else :
                self._curColIndex -= 1

    # Moves the cursor to the front of the current line.
    def moveLineHome( self ) :
        self._curColIndex = 0

    # Moves the cursor to the end of the current line.
    def moveLineEnd( self ) :
        self._curColIndex = self.numChars() - 1

    # Starts a new line at the cursor position.
    def breakLine( self ) :
        # Save the text following the cursor position.
        nlContents = self._curLine.text[ self._curColIndex: ]
        # Insert newline character and truncate the line.
        del self._curLine.text[ self._curColIndex: ]
        self._curLine.text.append( "\n" )
        # Insert the new line and increment the line counter.
        self._insertNode( self._curLine, nlContents )
        # Move the cursor
        self._curLine = newLine
        self._curLineIndex += 1
        self._curColIndex = 0

    # Inserts the given character at the current cursor position.
    def addChar( self, char ) :
        if char == "\n" :
            self.breakLine()
        else :
            index = self._curColIndex
            if self.inInsertMode() :
                self._curLine.text.insert( index, char )

            else :
                if self.getChar() == "\n" :
                    self._curLine.text.insert( index, char )
                else :
                    self._curLine.text[ index ] = char

                self._curColIndex += 1

    # Removes the character preceding the cursor; cursor remains fixed.
    def deleteChar( self ) :
        if self.getChar() != "\n" :
            self._curLine.text.pop( self._curColIndex )
        else :
            if self._curLine is self._lastLine :
                return

            else :
                nextLine = self._curLine.next
                self._curLine.text.pop()
                self._curLine.text.extend( nextLine.text )
                self._removeNode( nextLine )
# Storage class.
class _EditBufferNode :
    def __init__( self, text ) :
        self.text = text
        self.prev = None
        self.next = None

class MorseCodeTree :
    def __init__( self ) :
        self._root = _Node( None )

        self._root.left = _Node( None )
        self._root.right = _Node( None )

        self._buildTree( ".-", "A" )
        self._buildTree( "-...", "B" )
        self._buildTree( "-.-.", "C" )
        self._buildTree( "-..", "D" )
        self._buildTree( ".", "E" )
        self._buildTree( "..-.", "F" )
        self._buildTree( "--.", "G" )
        self._buildTree( "....", "H" )
        self._buildTree( "..", "I" )
        self._buildTree( ".---", "J" )
        self._buildTree( ".-..", "L" )
        self._buildTree( "--", "M" )
        self._buildTree( "-.", "N" )
        self._buildTree( "---", "O" )
        self._buildTree( ".--.", "P" )
        self._buildTree( "--.-", "Q" )
        self._buildTree( ".-.", "R" )
        self._buildTree( "...", "S" )
        self._buildTree( "-", "T" )
        self._buildTree( "..-", "U" )
        self._buildTree( "...-", "V" )
        self._buildTree( ".--", "W" )
        self._buildTree( "-.-", "K" )


    def _buildTree( self, seq, letter ) :

        if seq[0] == "." :
            self._insertNode( self._root.left, seq, letter )

        else :
            self._insertNode( self._root.right, seq, letter )


    def _insertNode( self, curNode, seq, letter ) :

        if len( seq ) == 1 :
            curNode.letter = letter

        else :
            if seq[1] == "." :
                if curNode.left is None :
                    node = _Node( None )
                    curNode.left = node
                    self._insertNode( curNode.left, seq[1:], letter )
                else :
                    self._insertNode( curNode.left, seq[1:], letter )

            elif seq[1] == "-" :
                if curNode.right is None :
                    node = _Node( None )
                    curNode.right = node
                    self._insertNode( curNode.right, seq[1:], letter )
                else :
                    self._insertNode( curNode.right, seq[1:], letter )

    def compute( self, codeSeq ) :

        word = ""

        for seq in codeSeq.split( " " ) :

            if seq[0] == "." :
                word += self._decode( self._root.left, seq[1:] )

            else :
                word += self._decode( self._root.right, seq[1:] )

        return word


    def _decode( self, curNode, seq ) :
        if len( seq ) < 1 :
            return curNode.letter

        elif seq[0] == "." :
            return self._decode( curNode.left, seq[1:] )
        else :
            return self._decode( curNode.right, seq[1:] )




class _Node :
    def __init__( self, letter ) :
        self.letter = letter
        self.left = None
        self.right = None

myTree = MorseCodeTree()
codeSeq = "- .-. . . ... .- .-. . ..-. ..- -."
word = myTree.compute( codeSeq )
print( word )
















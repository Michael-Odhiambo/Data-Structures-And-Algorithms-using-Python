
class Counter :

    def __init__( self ) :
        self._initialValue = 0

    def add( self ) :
        self._initialValue += 1

    def clear( self ) :
        self._initialValue = 0

    def display( self ) :
        return self._initialValue


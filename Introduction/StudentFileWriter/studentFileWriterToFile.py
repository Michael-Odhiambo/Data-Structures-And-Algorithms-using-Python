
class StudentFileWriter :

    def __init__( self, outputDest ) :
        self._outputDest = outputDest
        self._outputFile = None

    # Open the outputDest for writing.
    def open( self ) :
        self._outputFile = open( self._outputDest, "w" )

    # Close the outputDest after writing.
    def close( self ) :
        self._outputFile.close()
        self._outputFile = None

    # Write the records.
    def Write( self, record ) :
        self._outputFile.write( str( record ) )
            







        
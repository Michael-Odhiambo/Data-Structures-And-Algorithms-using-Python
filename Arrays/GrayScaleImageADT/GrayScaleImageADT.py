
from array2D import Array2D

class GrayscaleImage :
    
    # Creates a new instance that consists of nrows and ncols of pixels each set to an initial value of 0.
    def __init__( self, nrows, ncols ) :
        self._thePixels = Array2D( nrows, ncols )
        self._thePixels.clear( 0 )

    # Returns the width of the image.
    def width( self ) :
        return self._thePixels.numCols()

    # Returns the height of the image.
    def height( self ) :
        return self._thePixels.numRows()

    # Clears the entire image by setting each pixel to the given intensity value. The intensity value will be
    # clamped to 0 or 255 if it is less than 0 or greater than 255, respectively.
    def clear( self, value ) :
        if value < 0 :
            value = 0

        if value > 255 :
            value = 255

        self._thePixels.clear( value )

    # Returns the intensity level of the given pixel. The pixel coordinates must be within the valid range.
    def __getitem__( self, indexTuple ) :

        assert len( indexTuple ) == 2, "Invalid number of array subscripts."

        row = indexTuple[0]
        col = indexTuple[1]

        assert row >= 0 and row < self._thePixels.numRows() and col >= 0 and col < self._thePixels.numCols(),\
            "Index out of range."

        return self._thePixels[ row, col ]


    # Sets the intensity level of the given pixel to the given value. The pixel coordinates must be within
    # the valid range. The intensity value is clamped to 0 or 255 if it is outside the valid range.
    def __setitem__( self, indexTuple, value ) :

        assert len( indexTuple ) == 2, "Invalid number of array subscripts."

        row = indexTuple[0]
        col = indexTuple[1]

        assert row >= 0 and row < self._thePixels.numRows() and col >= 0 and col < self._thePixels.numCols(), \
            "Index out of range."

        if value < 0 :
            value = 0

        if value > 255 :
            value = 255

        self._thePixels[ row, col ] = value


myImage = GrayscaleImage( 10, 10 )
myImage.clear( 255 )

print( "Height : {}".format( myImage.height() ) )
print( "Width : {}".format( myImage.width() ) ) 

for row in range( myImage.height() ) :
    print( "--------------------------------------------------------------" )
    for col in range( myImage.width() ) :
        print( myImage[ row, col ], end = " | ")

    print()

print( "--------------------------------------------------------------" )



from array2D import Array2D

class ColorImage :

    # Creates a new instance that consists of nrows and ncols of pixels each set to black.
    def __init__( self, nrows, ncols ) :
        self._nRows = nrows
        self._nCols = ncols
        
        # The 2D array to store the individual pixels.
        self._the2DArray = Array2D( self._nRows, self._nCols )

        self.clear( _RGBColor() )

    # Returns the width of the image.
    def width( self ) :
        return self._nCols

    # Returns the height of the image.
    def height( self ) :
        return self._nRows

    # Returns the RGB color of the given pixel as an RGB color object. The pixel coordinates
    # must be within the valid range.
    def __getitem__(self, indexTuple ) :
        row = indexTuple[0]
        col = indexTuple[1]

        assert row >= 0 and row < self._nRows and col >= 0 and col < self._nCols, \
            "Indices out of range."

        return self._the2DArray[row, col]

    # Set the given pixel to the given RGB color. The pixel coordinates must be within the
    # valid range.
    def __setitem__( self, indexTuple, color ) :
        row = indexTuple[0]
        col = indexTuple[1]

        assert row >= 0 and row < self._nRows and col >= 0 and col < self._nCols, \
            "Indices out of range."

        self._the2DArray[row, col] = color


    # Clears the entire image by setting each pixel to the given RGB color (black).
    def clear( self, color ) :
        self._the2DArray.clear( color )

    

# Storage class.

class _RGBColor :
    def __init__( self, red = 0, green = 0, blue = 0 ) :
        self.red = red
        self.green = green
        self.blue = blue


# A color image can be easily converted to a grayscale image by converting each pixel of the color
    # image, specified by the three components ( R, G, B ), to a grayscale value using the formula
    
    #                  gray = round( 0.299 * R + 0.587 * G + 0.114 * B )

    # The proportions applied to each color component in the formula corresponds to the levels of
    # sensitivity with which humans see each of the three primary colors: red, green and blue.
    # Note the result from the equation must be converted capped to an integer in the range [0...255].
    # Use the equation and implement the function which accepts a ColorImage object as a argument
    # and creates and returns a new GrayscaleImage that is the grayscale version of the given color
    # image.

def colorToGrayScale( colorImg ) :
    # Go through every pixel in the colorImg.
    for row in range( colorImg.height() ) :
        for col in range( colorImg.width() ) :
            # Get the pixel.
            pixel = colorImg[ row, col ]
            # Convert the given pixel to grayScale.
            pixel = round( 0.299 * pixel.red + 0.587 * pixel.green + 0.144 * pixel.blue )

            colorImg[ row, col ] = pixel

    



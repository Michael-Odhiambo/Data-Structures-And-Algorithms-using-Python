
# Implements a Point class for representing points in the 2-D Cartesian coordinate system.

import math

class Point :
    # Creates a point object.
    def __init__( self, x, y ) :
        self.xCoord = x
        self.yCoord = y

    # Returns the x coordinate of the point.
    def getX( self ) :
        return self.xCoord

    # Returns the y coordinate of the point.
    def getY( self ) :
        return self.yCoord

    # Shifts the point by xInc and yInc.
    def shift( self, xInc, yInc ) :
        self.xCoord += xInc
        self.yCoord += yInc

    # Computes the distance between this point and the otherPoint.
    def distance( self, otherPoint ) :
        xDiff = self.xCoord - otherPoint.xCoord
        yDiff = self.yCoord - otherPoint.yCoord
        return math.sqrt( xDiff ** 2 + yDiff ** 2 )

    # Determines if two points are equal.
    def __eq__( self, rhsPoint ) :
        return self.xCoord == rhsPoint.xCoord and \
            self.yCoord == rhsPoint.yCoord

    # Determines if this point is at the origin.
    def isOrigin( self ) :
        origin = Point( 0, 0 )
        if self == origin :
            return True

        return False

    # Returns a string representation of the point.
    def __str__( self ) :
        return "(" + str(self.xCoord) + ", " + str(self.yCoord) + ")"



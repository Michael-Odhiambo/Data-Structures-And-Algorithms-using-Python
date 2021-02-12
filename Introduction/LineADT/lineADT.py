

from pointADT import Point

# Implements a LineSegment class constructed from Point objects.

class LineSegment :
    # Creates a line segment object.
    def __init__( self, fromPoint, toPoint ) :
        self._pointA = fromPoint
        self._pointB = toPoint

    # Gets the starting point of the line segment.
    def startPoint( self ) :
        return self._pointA

    # Gets the ending point of the line segment.
    def endPoint( self ) :
        return self._pointB

    # Gets the length of the line segment.
    def length( self ) :
        return self._pointA.distance( self._pointB )

    # Determines if the line is parallel to the y-axis.
    def isVertical( self ) :
        return self._pointA.getX() == self._pointB.getX()

    # Determines if the line is parallel to the x-axis.
    def isHorizontal( self ) :
        return self._pointA.getY() == self._pointB.getY()

    # Determines if this line is perpendicular to otherLine.
    # M1 * M2 = -1
    def isPerpendicular( self, otherLine ) :
        if self.slope() * otherLine.slope() == -1 :
            return True

        return False

    # Does this line segment intersect the otherLine.
    def intersects( self, otherLine ) :
        if self.slope() == otherLine.slope() :
            return False
        
        return True

    # Does this line segement bisect the otherLine.
    def bisects( self, otherLine ) :
        pass

    # Shifts the line segment by xInc amount along the x-axis and yInc amount along the y-axis.
    def shift( self, xInc, yInc ) :
        self._pointA.shift( xInc, yInc )
        self._pointB.shift( xInc, yInc )

    # Returns the midpoint of the line segment as a Point object.
    def midPoint( self ) :
        x = ( self._pointA.getX() + self._pointB.getX() ) / 2
        y = ( self._pointA.getY() + self._pointB.getY() ) / 2
        return Point( x, y )

    # Gets the slope of the line.
    def slope( self ) :
        if self.isVertical() : # not defined for a vertical line.
            return None

        else :
            run = self._pointA.getX() - self._pointB.getX()
            rise = self._pointA.getY() - self._pointB.getY()
            return rise / run






"""
By Michael Odhiambo.
03/12/2020  ~ 17:47

"""

import os

def dirSize( path ) :
    # Return the number of bytes used by a file/folder and any descendants.
    total = os.path.getsize( path )  # account for direct usage.
    # if this is a directory,
    if os.path.isdir( path ) :
        # then for each child:
        for filename in os.listdir( path ) :
            # compose full path to child.
            childPath = os.path.join( path, filename )
            # add child's size to total.
            total += dirSize( childPath )

    print( "{0:<7}".format( total), path )
    # return the grand total.
    return total

dirSize( "E:\\Music" )
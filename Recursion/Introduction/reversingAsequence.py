


def rev( S, start, stop ) :
    if start < stop - 1 :
        S[ start ], S[ stop - 1 ] = S[ stop - 1 ], S[ start ]
        rev( S, start + 1, stop - 1 )

rev( mySeq, 0, len(mySeq) )
print( mySeq )


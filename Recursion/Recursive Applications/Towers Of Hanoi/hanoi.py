
# Start with the whole stack.
def hanoi( n, source, destination, temp ) :
    if n >= 1 :
        # Move the top n - 1 disks from source to temp using destination.
        hanoi( n - 1, source, temp, destination )
        # Move the bottom disk to the destination rod.
        print( "Move {} to {}".format( source, destination ) )
        # Move the n - 1 disks from the temp rod to the destination using source.
        hanoi( n - 1, temp, destination, source )

print( hanoi( 3, 1, 3, 2 ) )

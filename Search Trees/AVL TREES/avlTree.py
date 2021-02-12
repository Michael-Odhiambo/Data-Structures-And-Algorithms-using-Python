
LEFT_HIGH = 1
EQUAL_HIGH = 0
RIGHT_HIGH = -1


# Storage class for creating the AVL tree node.
class _AVLMapNode :
    def __init__( self, key, value ) :
        self.key = key
        self.value = value
        self.bFactor = EQUAL_HIGH
        self.left = None
        self.right = None


class AVLMap :
    def __init__( self ) :
        self._root = None
        self._size = 0

    # Returns the size of the tree.
    def __len__( self ) :
        return self._size

    def _avlSearch( self, subTree, target ) :
        if subTree is None :  # Base case.
            return None

        elif target < subTree.key :  # Target is to the left of the subTree.
            return self._avlSearch( subTree.left, target )

        elif target > subTree.key :  # Target is to the right of the subTree.
            return self._avlSearch( subTree.right, target )

        else :  # target has been found.
            return subTree

    # Helper method for finding the node containing the minimum key.
    def _avlMinimum( self, subTree ) :
        if subTree is None :
            return None
        elif subTree.left is None :
            return subTree
        else :
            return self._avlMinimum( subTree.left )

    # Determines if the given key is contained in the tree.
    def __contains__( self, key ) :
        return self._avlSearch( self._root, key ) is not None

    def add( self, key, value ) :
        node = self._avlSearch( self._root, key )
        if node is not None :
            node.value = value
            return False

        else :
            self._root, tmp = self._avlInsert( self._root, key, value )
            self._size += 1
            return True

    # Removes the map entry associated with the given key.
    def remove( self, key ) :
        assert key in self, " Invalid map key. "
        self._root = self._avlRemove( self._root, key )
        self._size -= 1

    # Helper method for removing an entry from the AVL tree.
    def _avlRemove( self, subTree, target ) :
        # Search for the item in the tree.
        # See if we need to move to the left.
        if target < subTree.key :
            subTree.left = self._avlRemove( subTree.left, target )

            # Adjust the balance factors appropriately.
            if subTree.bFactor == RIGHT_HIGH :
                subTree = self._avlRightBalance( subTree )

            return subTree

        # Otherwise, move to the right.
        elif target > subTree.key :
            subTree.right = self._avlRemove( subTree.right, target )

            if subTree.bFactor == LEFT_HIGH :
                subTree = self._avlLeftBalance( subTree )

            return subTree

        # We found the node containing the key.
        else :
            if subTree.left is None and subTree.right is None :  # Leaf Node.
                return None

            elif subTree.left is None or subTree.right is None :  # Single child.
                if subTree.left is not None :
                    return subTree.left
                else :
                    return subTree.right

            else :  # Interior node with two children.
                # Find its successor within the tree.
                successor = self._avlMinimum( subTree.right )
                subTree.key = successor.key
                subTree.value = successor.value
                subTree.right = self._avlRemove( subTree.right, successor.key )
                return subTree


    def valueOf( self, key ) :
        node = self._avlSearch( self._root, key )
        assert node is not None, "Invalid map key."
        return node.value

    def __iter__( self ) :
        pass

    # Recursive method to handle the insertion into an AVL tree. The function returns a tuple containing a reference
    # to the root of the subtree and a boolean to indicate if the subtree grew taller.
    def _avlInsert( self, subTree, key, newItem ) :
        # See if we have found the insertion point.
        if subTree is None :
            subTree = _AVLMapNode( key, newItem )
            taller = True

        # Is the key already in the tree?
        elif key == subTree.key :
            taller = False
            return subTree, taller

        # See if we need to navigate to the left.
        elif key < subTree.key :
            subTree.left, taller = self._avlInsert( subTree.left, key, newItem )

            # If the subtree grew taller, see if it needs re-balancing.
            if taller :
                if subTree.bFactor == LEFT_HIGH :
                    subTree = self._avlLeftBalance( subTree )
                    taller = False

                elif subTree.bFactor == EQUAL_HIGH :
                    subTree.bFactor = LEFT_HIGH
                    taller = True

                else :
                    subTree.bFactor = EQUAL_HIGH
                    taller = False

        # Otherwise, navigate to the right.
        else :
            subTree.right, taller = self._avlInsert( subTree.right, key, newItem )
            # If the subtree grew taller, see if it needs re-balancing.

            if taller :
                if subTree.bFactor == LEFT_HIGH :
                    subTree.bFactor = EQUAL_HIGH
                    taller = False

                elif subTree.bFactor == EQUAL_HIGH :
                    subTree.bFactor = RIGHT_HIGH
                    taller = True

                else :
                    subTree = self._avlRightBalance( subTree )
                    taller = False

        return subTree, taller

    # Rebalance a tree when its right subtree is higher.
    def _avlRightBalance( self, pivot ) :
        # Set C to point to the right child of the pivot.
        C = pivot.right

        # See if the re-balance is due to case 3.
        if C.bFactor == RIGHT_HIGH :
            pivot.bFactor = EQUAL_HIGH
            C.bFactor = EQUAL_HIGH
            pivot = self._avlRotateLeft( pivot )
            return pivot

        # Otherwise, a balance from the right is due to case 4.
        else :
            G = C.left

            # Change the balance factors.
            if G.bFactor == LEFT_HIGH :
                pivot.bFactor = EQUAL_HIGH
                C.bFactor = RIGHT_HIGH

            elif G.bFactor == RIGHT_HIGH :
                C.bFactor = EQUAL_HIGH
                pivot.bFactor = LEFT_HIGH

            else :
                C.bFactor = EQUAL_HIGH
                pivot.bFactor = EQUAL_HIGH

            # All three cases set G's balance factor to EQUAL_HIGH.
            G.bFactor = EQUAL_HIGH

            # Perform the double rotation.
            pivot.right = self._avlRotateRight( C )
            pivot = self._avlRotateLeft( pivot )

            return pivot

    # Rebalance a node when its left subtree is higher.
    def _avlLeftBalance( self, pivot ) :

        # Set C to point to the left child of the pivot.
        C = pivot.left

        # See if the re-balancing is due to case 1.
        if C.bFactor == LEFT_HIGH :
            pivot.bFactor = EQUAL_HIGH
            C.bFactor = EQUAL_HIGH
            pivot = self._avlRotateRight( pivot )

            return pivot

        # Otherwise, a balance from the left is due to case 2.
        else :
            G = C.right

            # Change the balance factors.
            if G.bFactor == LEFT_HIGH :
                pivot.bFactor = RIGHT_HIGH
                G.bFactor = EQUAL_HIGH

            elif G.bFactor == EQUAL_HIGH :
                pivot.bFactor = EQUAL_HIGH
                C.bFactor = EQUAL_HIGH

            else :
                pivot.bFactor = EQUAL_HIGH
                C.bFactor = LEFT_HIGH

            # All three cases set G's balance factor to EQUAL_HIGH.
            G.bFactor = EQUAL_HIGH

            # Perform the double rotation.
            pivot.left = self._avlRotateLeft( C )
            pivot = self._avlRotateRight( pivot )

            return pivot

    # Rotates the pivot to the right around its left child.
    def _avlRotateRight( self, pivot ) :
        C = pivot.left
        pivot.left = C.right
        C.right = pivot

        return C

    # Rotates the pivot to the left around its right child.
    def _avlRotateLeft( self, pivot ) :
        C = pivot.right
        pivot.right = C.left
        C.left = pivot

        return C

myTree = AVLMap()
myTree.add( 60, "Michael" )
myTree.add( 25, "Allan" )
myTree.add( 100, "Odhiambo" )
myTree.add( 17, "Post" )
myTree.add( 30, "Chris" )
myTree.add( 80, "Ryde" )
myTree.add( 120, "Ryde" )
myTree.add( 28, "Ryde" )
myTree.add( 35, "Ryde" )

myTree.remove( 100 )
print( myTree._root.key )
print( myTree._root.left.key )
print( myTree._root.left.left.key )
print( myTree._root.left.right.key )
print( myTree._root.right.key )
print( myTree._root.right.left.key )
print( myTree._root.right.right.key )
print( myTree._root.right.right.left.key )
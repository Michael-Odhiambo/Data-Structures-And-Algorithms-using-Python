
from arrayADT import Array
from lListStack import Stack

class BSTMap :

    # Creates an empty map instance.
    def __init__( self ) :
        self._root = None
        self._size = 0

    # Returns the number of entries in the map.
    def __len__( self ) :
        return self._size

    # Returns an iterator for traversing the keys in the map.
    def __iter__( self ) :
        return _BSTMapIterator1( self._root )

    # Helper method that recursively searches the tree for the target key.
    def _bstSearch( self, subTree, target ) :
        if subTree is None :  # Base case.
            return None

        elif target < subTree.key :  # Target is to the left of the subTree.
            return self._bstSearch( subTree.left, target )

        elif target > subTree.key :  # Target is to the right of the subTree.
            return self._bstSearch( subTree.right, target )

        else :  # target has been found.
            return subTree

    # Determines if the map contains the given key.
    def __contains__( self, key ) :
        return self._bstSearch( self._root, key ) is not None

    # Returns the value associated with the key.
    def valueOf( self, key ) :
        node = self._bstSearch( self._root, key )
        assert node is not None, " Invalid key entry. "
        return node.value

    # Helper method for finding the node containing the minimum key.
    def _bstMinimum( self, subTree ) :
        if subTree is None :
            return None
        elif subTree.left is None :
            return subTree
        else :
            return self._bstMinimum( subTree.left )

    # Adds a new entry to the map or replaces the value of an existing key.
    def add( self, key, value ) :
        # Find the node containing the key, if it exists.
        node = self._bstSearch( self._root, key )
        # If the key is already in the tree, update its value.
        if node is not None :
            node.value = value
            return False

        # Otherwise, add a new entry.
        else :
            self._root = self._bstInsert( self._root, key, value )
            self._size += 1
            return True

    # Helper method that inserts a new item, recursively.
    def _bstInsert( self, subTree, key, value ) :
        if subTree is None :
            subTree = _BSTMapNode( key, value )
        elif key < subTree.key :
            subTree.left = self._bstInsert( subTree.left, key, value )
        elif key > subTree.key :
            subTree.right = self._bstInsert( subTree.right, key, value )

        return subTree

    # Removes the map entry associated with the given key.
    def remove( self, key ) :
        assert key in self, " Invalid map key. "
        self._root = self._bstRemove( self._root, key )
        self._size -= 1



    # Helper method that removes an existing item recursively.
    def _bstRemove( self, subTree, target ) :
        # Search for the item in the tree.
        if target < subTree.key :
            subTree.left = self._bstRemove( subTree.left, target )
            return subTree

        elif target > subTree.key :
            subTree.right = self._bstRemove( subTree.right, target )
            return subTree

        # We found the node containing the item.
        else :
            if subTree.left is None and subTree.right is None :  # Leaf node.
                return None

            elif subTree.left is None or subTree.right is None :  # Single child.
                if subTree.left is not None :
                    return subTree.left
                else :
                    return subTree.right

            else :  # Has two children.
                successor = self._bstMinimum( subTree.right )
                subTree.key = successor.key
                subTree.value = successor.value
                subTree.right = self._bstRemove( subTree.right, successor.key )
                return subTree


# Storage class for the nodes.
class _BSTMapNode :
    def __init__( self, key, value ) :
        self.key = key
        self.value = value
        self.left = None
        self.right = None

# An iterator for the binary search tree using an array.
class _BSTMapIterator :
    def __init__( self, root, size ) :
        # Creates the array and fills it with the keys.
        self._theKeys = Array( size )
        self._curItem = 0  # Keep track of the current location in the array.
        self._bstTraversal( root )
        self._curItem = 0  # Reset the current item index.

    def __iter__( self ) :
        return self

    # Returns the next key from the array of keys.
    def __next__( self ) :
        if self._curItem < len( self._theKeys ) :
            key = self._theKeys[ self._curItem ]
            self._curItem += 1
            return key

        else :
            raise StopIteration

    # Performs an inorder traversal use to build the array of keys.
    def _bstTraversal( self, subTree ) :
        if subTree is not None :
            self._bstTraversal( subTree.left )
            self._theKeys[ self._curItem ] = subTree.key
            self._curItem += 1
            self._bstTraversal( subTree.right )


# An iterator for the binary search tree using a software stack.
class _BSTMapIterator1 :
    def __init__( self, root ) :
        # Create a stack for use in traversing the tree.
        self._theStack = Stack()

        # We must traverse down the node containing the smallest key
        # during which each node along the path is pushed onto the stack.
        self._traverseToMinNode( root )

    def __iter__( self ) :
        return self

    # Returns the next item from the BST in key order.
    def __next__( self ) :
        # If the stack is empty, we are done.
        if self._theStack.isEmpty() :
            raise StopIteration

        else :
            # The top node on the stack contains the next key.
            node = self._theStack.pop()
            key = node.key
            # If this node has a subtree rooted as the right child, we must find
            # the node in that subtree that contains the smallest key.
            # Again, the nodes along the path are pushed onto the stack.
            if node.right is not None :
                self._traverseToMinNode( node.right )

            return key

    # Traverses down the subtree to find the node containing the smallest key
    # during which the nodes along that path are pushed onto the stack.
    def _traverseToMinNode(self, subTree ) :
        if subTree is not None :
            self._theStack.push( subTree )
            self._traverseToMinNode( subTree.left )

myTree = BSTMap()
myTree.add( 60, "Michael" )
myTree.add( 12, "Allan" )
myTree.add( 90, "Odhiambo" )
myTree.add( 4, "Steve" )
myTree.add( 41, "Larry" )
myTree.add( 71, "Sonny" )
myTree.add( 100, "Tommy" )
myTree.add( 1, "Biden" )
myTree.add( 29, "Carl" )
myTree.add( 84, "Vercetti" )
myTree.add( 23, "Peter" )
myTree.add( 37, "Johnson" )
print( len( myTree ) )
myTree.remove( 60 )
print( len( myTree ) )
print( myTree._root.key )

for key in myTree :
    print( key )

# The storage class for creating binary tree nodes.
class _BinTreeNode :
    def __init__( self, data ) :
        self.data = data
        self.left = None
        self.right = None


# TREE TRAVERSALS.

# Preorder Traversal.

# A tree traversal must begin with the root node, since that is the only access into
# the tree. After visiting the root node, we can then traverse the nodes in its left
# followed by the nodes in its right subtree. Since every node is the root
# of its own subtree, we can repeat the same process on each node, resulting in a
# recursive solution. The base case occurs when a null child link is encountered since
# there will be no subtree to be processed from that link.

# This traversal in known as preorder traversal since we first visit the node followed by
# the subtree traversals.

# The subtree argument will either be a null reference or a reference to the root of a
# subtree in the binary tree. If the reference is not None, the node is first visited and then
# the two subtrees are traversed. By convention, the left subtree is always visited before
# the right subtree. The subtree argument will be a null reference when the binary tree is empty
# or we attempt to follow a non-existent link for one or both of the children.

# Given a binary tree of size n, a complete traversal of a binary tree visits each node once.
# If the visit operation only requires constant time, the tree traversal can be done in O( n ) time.

def preOrderTrav( subTree ) :
    if subTree is not None :
        print( subTree.data )
        preOrderTrav( subTree.left )
        preOrderTrav( subTree.right )

# Inorder Traversal.

# In the preorder traversal, we chose to first visit the node and then traverse both
# subtrees. Another traversal that can be performed is the inorder traversal, in which
# we first traversal the left subtree and then visit the node followed by the traversal
# of the right subtree.

def inOrderTrav( subTree ) :
    if subTree is not None :
        inOrderTrav( subTree.left )
        print( subTree.data )
        inOrderTrav( subTree.right )


# Postorder Traversal.

# We can also perform a postorder traversal, which cann be viewed as the opposite of the
# preorder traversal. In a postorder traversal, the left and right subtrees of each
# node are traversed before the node is visited.

def PostOrderTrav( subTree ) :
    if subTree is not None :
        PostOrderTrav( subTree.left )
        PostOrderTrav( subTree.right )
        print( subTree.data )


# Bread-First Traversal.

# The preorder, inorder and postorder traversals are all examples of a depth-first traversal.
# That is, the nodes are traversed deeper in the tree before returning to higher-level nodes.
# Another type of traversal that can be performed on a binary tree is the breadth-first traversal.
# In a breadth-first traversal, the nodes are visited by level, from left to right.

# Recursion cannot be used to implement a breadth-first traversal since the recursive calls must
# follow the links that lead deeper into the tree. Instead, we must devise another approach.

def breadthFirstTrav( binTree ) :
    # Create a queue and add the root node to it.
    theQueue = Queue()
    theQueue.enqueue( binTree )

    # Visit each node in the Tree.
    while not theQueue.isEmpty() :
        # Remove the next node from the queue and visit it.
        node = theQueue.dequeue()
        print( node.data )

        # Add the two children to the queue.
        if node.left is not None :
            theQueue.enqueue( node.left )
        if node.right is not None :
            theQueue.enqueue( node.right )


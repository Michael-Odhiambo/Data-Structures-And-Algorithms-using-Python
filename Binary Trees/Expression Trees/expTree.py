
from queue import Queue

class ExpressionTree :

    # Builds an expression tree for expression string.
    def __init__( self, expStr ) :
        self._expTree = None
        self._buildTree( expStr )
        print( self._expTree.left.element )

    # Evaluates the expression tree and returns the resulting value.
    def evaluate( self, varMap ) :
        return self._evalTree( self._expTree, varMap )

    # Returns a string representation of the expression tree.
    def __str__( self ) :
        return self._buildString( self._expTree )

    # Recursively builds a string representation of the expression tree.
    def _buildString( self, treeNode ) :
        # If the node is a leaf, it's an operand.
        if treeNode.left is None and treeNode.right is None :
            return str( treeNode.element )

        else : # Otherwise, its an operator.
            expStr = " ( "
            expStr += self._buildString( treeNode.left )
            expStr += treeNode.element
            expStr += self._buildString( treeNode.right )
            expStr += " ) "

            return expStr

    # Tree Evaluation.

    # Given an algebraic expression represented as a binary tree, we can develop an
    # algorithm to evaluate the expression. Each subtree represents a valid subexpression
    # with those lower in the tree having higher precedence. Thus, the two subtrees
    # each interior node must be evaluated before the node itself.
    def _evalTree( self, subTree, varDict ) :
        # See if the node is a leaf node, in which case return its value.
        if subTree.left is None and subTree.right is None :
            # Is the operand a literal digit?
            if subTree.element >= "0" and subTree.element <= "9" :
                return int( subTree.element )

            else : # Or is it a variable?
                assert subTree.element in varDict , " Invalid variable."
                return varDict[ subTree.element ]

        # Otherwise, it's an operator that needs to be computed.
        else :
            # Evaluate the expression in the left and right subtrees.
            lValue = self._evalTree( subTree.left, varDict )
            rValue = self._evalTree( subTree.right, varDict )

            # Evaluate the operator using a helper method.
            return self._computeOp( lValue, subTree.element, rValue )

    # Compute the arithmetic operation based on the supplied op string.
    def _computeOp( self, left, op, right ) :

        if op == "+" :
            result = left + right

        elif op == "-" :
            result = left - right

        elif op == "/" :
            result = left / right

        elif op == "*" :
            result = left * right

        elif op == "%" :
            result = left % right

        return result

    # TREE CONSTRUCTION.

    # We have seen how an expression tree is used; now lets look at how to construct the tree given
    # an infix expression. For simplicity, we assume the following: (1) the expression is stored in
    # string with no white space; (2) the supplied expression is valid and fully parenthesized; (3) each
    # operand will be a single-digit or single-letter variable; and (4) the operators will consist of
    # +, -, *, / and %.
    def _buildTree( self, expStr ) :
        # Build a queue containing the tokens in the expression string.
        expQ = Queue()
        for token in expStr :
            #print( token )
            expQ.enqueue( token )

        # Create an empty root node.
        self._expTree = _ExpTreeNode( None )
        # Call the recursive function to build the expression tree.
        self._recBuildTree( self._expTree, expQ )

    # Recursively builds the tree given an initial root node.
    def _recBuildTree( self, curNode, expQ ) :
        # Extract the next token from the queue.
        token = expQ.dequeue()

        # See if the token is a left paren: "(".
        if token == "(" :
            curNode.left = _ExpTreeNode( None )
            self._recBuildTree( curNode.left, expQ )

            # The next token will be an operator.
            curNode.element = expQ.dequeue()
            curNode.right = _ExpTreeNode( None )
            self._recBuildTree( curNode.right, expQ )

            # The next token will be a ), remove it.
            expQ.dequeue()

        # Otherwise, the token is a digit that has to be converted to an int.
        else :
            curNode.element = token





# Storage class for creating the tree nodes.
class _ExpTreeNode :
    def __init__( self, data ) :
        self.element = data
        self.left = None
        self.right = None


# Create a dictionary containing values for the one-letter variables.
vars = { 'a' : 5, 'b' : 12 }
# Build the tree for a sample expression and then evaluate it.
expTree = ExpressionTree( "(a/(b-3))" )
print( expTree )
print( "The result = ", expTree.evaluate(vars) )

print( 5 / 9 )

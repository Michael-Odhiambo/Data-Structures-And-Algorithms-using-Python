
from theStack import Stack
import math

# We can design and build a postfix calculator to perform simple arithmetic operations. The calculator consists
# of a single storage component that consists of an operand stack. The operations performed by the stack always
# uses the top two values in the stack and store the results back on the top of the stack.

class PostFixCalculator :

    # Creates a new postfix calculator with an empty operand stack.
    def __init__( self ) :
        self._theStack = Stack()

        # Second stack where values can be saved.
        self._saveStack = Stack()

    # Pushes the given operand "x" onto the top of the stack.
    def pushValue( self, x ) :
        self._theStack.push( x )

    # Returns an alias to the value currently on top of the stack. If the stack is empty, None
    # is returned.
    def result( self ) :
        if self._theStack.isEmpty() :
            return None

        return self._theStack.peek()

    # Clears the entire contents of the stack.
    def clear( self ) :
        for val in range( len( self._theStack ) ) :
            self._theStack.pop()

        return self._theStack.isEmpty()

    # Removes the top entry from the stack and discards it.
    def clearLast( self ) :
        self._theStack.pop()

    # Removes the top item from the operand stack and pushes it onto the save stack.
    def store( self ) :
        val = self._theStack.pop()
        self._saveStack.push( val )

    # Removes the top item from the save stack and pushes it onto the operand stack.
    def recall( self ) :
        val = self._saveStack.pop()
        self._theStack.push( val )

    # Removes the top two values from the stack and applies the given operation to those values. The first value
    # removed from the stack is the right-hand side operand and the second is the left hand side operand. The result
    # of this operation is pushed back to the stack. The operation is specified as a string containing one of
    # the operators + - * / **.
    def compute( self, op ) :

        ops1 = [ "abs", "sqrt", "sin", "cos", "tan" ]

        if op in ops1 :
            assert not self._theStack.isEmpty(), " Error!! "
            val = self._theStack.pop()

            if op == "abs" :
                val = abs( val )
                self._theStack.push( val )

            elif op == "sqrt" :
                val = math.sqrt( val )
                self._theStack.push( val )

            elif op == "sin" :
                val = math.sin( val )
                self._theStack.push( val )

            elif op == "cos" :
                val = math.cos( val )
                self._theStack.push( val )

            elif op == "tan" :
                val = math.tan( val )
                self._theStack.push( val )

        else :

            assert not self._theStack.isEmpty(), " Error!! Too many operators. "
            y = int(self._theStack.pop())

            assert not self._theStack.isEmpty(), " Error!! Too many operators. "
            x = int(self._theStack.pop())

            if op == "+":
                result = x + y
                self._theStack.push(result)

            elif op == "-":
                result = x - y
                self._theStack.push(result)

            elif op == "*":
                result = x * y
                self._theStack.push(result)

            elif op == "/":
                result = x / y
                self._theStack.push(result)

            elif op == "**":
                result = x ** y
                self._theStack.push(result)










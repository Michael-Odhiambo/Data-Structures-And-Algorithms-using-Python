
from theStack import Stack
import math

def solveExpression() :

    prompt = " Enter the postfix expression to evaluate: "
    expression = input( prompt )
    myStack = Stack()
    operators = [ "+", "-", "*", "/", "abs", "sqrt", "sin", "cos", "tan" ]

    for token in expression.split() :
        if token in operators :
            if token == "abs" :
                val = myStack.pop()
                val = abs( val )
                myStack.push( val )

            elif token == "sqrt" :
                val = myStack.pop()
                val = math.sqrt( val )
                myStack.push( val )

            elif token == "sin" :
                val = myStack.pop()
                val = math.sin( val )
                myStack.push( val )

            elif token == "cos" :
                val = myStack.pop()
                val = math.cos( val )
                myStack.push( val )

            elif token == "tan" :
                val = myStack.pop()
                val = math.tan( val )
                myStack.push( val )

            else :

                assert not myStack.isEmpty(), " Error!! Too many operators. "
                y = int(myStack.pop())

                assert not myStack.isEmpty(), " Error!! Too many operators. "
                x = int(myStack.pop())

                if token == "+":
                    result = x + y
                    myStack.push(result)

                elif token == "-":
                    result = x - y
                    myStack.push(result)

                elif token == "*":
                    result = x * y
                    myStack.push(result)

                elif token == "/":
                    result = x / y
                    myStack.push(result)

        else :
            myStack.push( token )


    answer = myStack.pop()
    assert myStack.isEmpty(), " Error!! Too many operands. "

    print( answer )

solveExpression()




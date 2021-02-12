
from postFixCalculatorADT import PostFixCalculator

operators = [ '+', '-', '*', '/', 'abs', 'sin', 'cos', 'tan' ]
calculator = PostFixCalculator()
command = input(" : " )

if command == "Enter" :
    while True :
        value = input( " Enter Value : " )

        if value == "Result" :
            print( calculator.result() )
            break

        elif value in operators :
            calculator.compute( value )

        else :
            calculator.pushValue( value )







# A python implementation of the validation algorithm is provided below. The funtion accepts a file object,
# which we assume was previously open and contains c++ source code. The file is scanned one line at a time
# to determine if it contains properly paired and balanced delimiters. A stack is used to store the opening
# delimiters and either implementation can be used since the implementation is dependent of the definition.
# Here, we have chosen to use the linked list implementation. As the file is scanned, we need only examine the
# characters that correspond to one of the three types of delimiter pairs. All other characters can be ignored.
# When an opening delimiter is encountered, we push it onto the stack. When a closing delimiter occurs, we 
# first check to make sure the stack is not empty. If it is empty, then the delimiters are not properly paired
# and balanced and no further processing is needed. We terminate the function and return False. When the stack
# is not empty, the top item is popped and compared to the closing delimiter. The two delimiters do match 
# corresponding opening and closing delimiters; we again terminate the function and return False. Finally, 
# after the entire file is processed, the stack should be empty when the delimiters are properly paired 
# and balanced. For the final test, we check to make sure the stack is empty and return either True or False,
# accordingly.

# Implementation of the algorithm for validating balanced brackets in
# a C++ source file.

from lListStack import Stack


def isValidSource( srcFile ) :
    s = Stack()
    for line in srcFile :
        for token in line :
            if token in "{[(" :
                s.push( token )
            
            elif token in "}])" :
                if s.isEmpty() :
                    return False

                else :
                    left = s.pop()
                    if ( token == "}" and left != "{" ) or ( token == "]" and left != "[" ) or \
                        ( token == ")" and left != "(" ) :
                        return False

    return s.isEmpty()

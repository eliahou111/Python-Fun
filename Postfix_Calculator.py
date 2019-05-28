
# Author: Eliahou Mayor 

import operator

# ArrayStack Class, postfix calculator is on line 34
class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data.pop()

# Functions for postfix calculator Q3

def readExpression():
    """
    This function reads the expression from the command line and returns it in a list
    """
    line = input("--> ").rstrip()
    return line.split(' ') 

def postfixCalculator():
    # supported operations, to add more operations just insert in the dict like below
    operations = {"+" : operator.add, "-": operator.sub, "*":operator.mul, "/": operator.truediv,
                    "**": operator.pow, "%": operator.mod,  "//" : operator.floordiv}
    variables = {}  # holds variables 

    line = readExpression()
    while line[0] != "done()":
        s = ArrayStack()    # stack to keep track of final value
        assignment = False
        for val in line:

            if val.isdigit():   # if it's a number, push to stack
                s.push(eval(val))

            elif val in operations:     # if it's an operator 
                b = s.pop()
                if b in variables:  # if it's a variable with a value
                    b = variables[b]
                a = s.pop()
                if a in variables:
                    a = variables[a]
                s.push(operations[val](a,b))    # push the value after the operation

            elif (val == "="):    # if expression contains an assignment
                assignment = True

            else:       # anything else is a variable name
                s.push(val)     # add new variable
        if assignment:      # if we need to assign a value
            value = s.pop()
            char = s.pop()
            variables[char] = value     # add/update variable dictionary
            print(char)     # return variable name            
        else:   
            if s.top() in variables:    # if remaining value is a variable
                print(variables[s.pop()])   # print the variable name
            else:
                print(s.pop())  # print final value
        line = readExpression()     # read next line
def main():
    return postfixCalculator()
if __name__ == '__main__':
    main()

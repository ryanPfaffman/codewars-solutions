'''
This time we want to write calculations using functions and get the results.
Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations:
plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function
represents the right operand
Division should be integer division. For example, this should return 2, not
2.666666...:
'''

def plus(function):
    string = 'plus'
    return [function, string]

def minus(function):
    string = 'minus'
    return [function, string]

def times(function):
    string = 'times'
    return [function, string]

def divided_by(function):
    string = 'divided_by'
    return [function, string]

def zero(function = None):
    if function:
        if function[1] == 'plus':
            return 0 + function[0]
        elif function[1] == 'minus':
            return 0 - function[0]
        elif function[1] == 'times':
            return 0 * function[0]
        elif function[1] == 'divided_by':
            return int(0 / function[0])
    return 0


def one(function = None):
    if function:
        if function[1] == 'plus':
            return 1 + function[0]
        elif function[1] == 'minus':
            return 1 - function[0]
        elif function[1] == 'times':
            return 1 * function[0]
        elif function[1] == 'divided_by':
            return int(1 / function[0])
    return 1

def two(function = None):
    if function:
        if function[1] == 'plus':
            return 2 + function[0]
        elif function[1] == 'minus':
            return 2 - function[0]
        elif function[1] == 'times':
            return 2 * function[0]
        elif function[1] == 'divided_by':
            return int(2 / function[0])
    return 2

def three(function = None):
    if function:
        if function[1] == 'plus':
            return 3 + function[0]
        elif function[1] == 'minus':
            return 3 - function[0]
        elif function[1] == 'times':
            return 3 * function[0]
        elif function[1] == 'divided_by':
            return int(3 / function[0])
    return 3

def four(function = None):
    if function:
        if function[1] == 'plus':
            return 4 + function[0]
        elif function[1] == 'minus':
            return 4 - function[0]
        elif function[1] == 'times':
            return 4 * function[0]
        elif function[1] == 'divided_by':
            return int(4 / function[0])
    return 4

def five(function = None):
    if function:
        if function[1] == 'plus':
            return 5 + function[0]
        elif function[1] == 'minus':
            return 5 - function[0]
        elif function[1] == 'times':
            return 5 * function[0]
        elif function[1] == 'divided_by':
            return int(5 / function[0])
    return 5

def six(function = None):
    if function:
        if function[1] == 'plus':
            return 6 + function[0]
        elif function[1] == 'minus':
            return 6 - function[0]
        elif function[1] == 'times':
            return 6 * function[0]
        elif function[1] == 'divided_by':
            return int(6 / function[0])
    return 6

def seven(function = None):
    if function:
        if function[1] == 'plus':
            return 7 + function[0]
        elif function[1] == 'minus':
            return 7 - function[0]
        elif function[1] == 'times':
            return 7 * function[0]
        elif function[1] == 'divided_by':
            return int(7 / function[0])
    return 7

def eight(function = None):
    if function:
        if function[1] == 'plus':
            return 8 + function[0]
        elif function[1] == 'minus':
            return 8 - function[0]
        elif function[1] == 'times':
            return 8 * function[0]
        elif function[1] == 'divided_by':
            return int(8 / function[0])
    return 8

def nine(function = None):
    if function:
        if function[1] == 'plus':
            return 9 + function[0]
        elif function[1] == 'minus':
            return 9 - function[0]
        elif function[1] == 'times':
            return 9 * function[0]
        elif function[1] == 'divided_by':
            return int(9 / function[0])
    return 9

'''
At first, I tried to solve this by adding a .has_been_called method to the plus
operator functions, and if those functions had been called in the operand
functions, change the .has_been_called to True. Outside of the function, it
changed back to False.

Example:
def plus(function):
  plus.has_been_called = True
  return function
plus.has_been_called = False

def one(function = None):
    if function:
        if plus.has_been_called == True:
            plus.has_been_called = False
            return 1 + function
        elif minus.has_been_called == True:
            minus.has_been_called = False
            return 1 - function
        elif times.has_been_called == True:
            times.has_been_called = False
            return 1 * function
        elif divided_by.has_been_called == True:
            divided_by.has_been_called = False
            return int(1 / function)

    return 1

When I tried to pass the Kata using this method, I got the four sample tests to
pass, but when I tried to run the code against the 164 other tests, I eventually
failed every time. The number of failures ranged from 11 to 46!
I am not sure why this is. The code would call the operator called previously
on the number functions. For example, if six(times(eight())) had been
successfully called and then six(divided_by(eight())) was called afterwards,
the output of the second function would be 48.

So, I found an easier way to do it by returning a list of both the function
and a string. In the operand functions, I checked to see what the string was.
Simple. I am still taking a long time to figure out these simple solutions, but
I feel my thought-processes improving, so that is good I guess.
'''

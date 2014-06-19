#!/bin/python3

"""
@author Arun George, 2014
@desc Parentheses balance check using Stack data structure
@usage: (()) - returns True; (() - returns False
"""


class Stack:
    """ Creation of stack data structure """

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def par_check(str):
    """ Check if parentheses are balanced or not """

    s = Stack()
    balanced = True
    index = 0

    while index < len(str) and balanced:
        symbol = str[index]

        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index += 1


    if balanced and s.isEmpty():
        return "Parentheses are balanced!"
    else:
        return "Not balanced!"


def main():
    prompt = str(input("Enter a sequence to parentheses to check if it's balanced..."))
    print(par_check(prompt))

main()
"""
Author: Jaemin Park
Date: 19/07/2025

Implementation of minimum stack

Description:
Allows one to find the smallest element of a stack in O(1) time. 

Approach:
Instead of pushing single elements, we push the element alongside the minimum of the stack up to that point
in the format: (element, minimum of stack up to this point)
"""

class Stack:
    def __init__(self):
        self.elements = []
        self.size = 0

    def size(self):
        return self.size
    
    def push(self, element):
        self.elements.append(element)
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError

        self.size -= 1 

        return self.elements.pop(self.size)
    
    def peek(self):
        if self.size == 0:
            raise IndexError
        
        return self.elements[self.size - 1]
    
class MinimumStack:
    ELEMENT = 0
    CUR_MINIMUM = 1

    def __init__(self):
        self.stack = Stack()

    def push(self, element):
        prev_minimum = element
        if self.stack.size() > 0:
            prev_minimum = self.stack.peek()[self.CUR_MINIMUM]
        
        self.stack.push((element, prev_minimum))

    def pop(self):
        return self.stack.pop()[self.ELEMENT]
    
    def peek(self):
        return self.stack.peek()[self.ELEMENT]
    
    def get_minimum(self):
        return self.stack.peek()[self.CUR_MINIMUM]
from collections import deque

class MinimumStack:
    ELEMENT = 0
    MINIMUM = 1

    def __init__(self):
        self.stack = deque()
        self.size = 0

    def push(self, element: int):
        cur_minimum = element
        if self.size > 0:
            top_element = self.stack.pop()
            cur_minimum = min(top_element[self.MINIMUM], cur_minimum)
            self.stack.append(top_element)

        new_element = (element, cur_minimum)

        self.stack.append(new_element)
        self.size += 1
    
    def pop(self) -> int:
        if self.size == 0:
            raise IndexError
        
        top_element = self.stack.pop()

        self.size -= 1

        return top_element[self.ELEMENT]

    def peek(self) -> int:
        if self.size == 0:
            raise IndexError
        
        top_element = self.stack.pop()
        cur_minimum = top_element[self.ELEMENT]
        self.stack.append(top_element)

        return cur_minimum
    
    def get_minimum(self) -> int:
        if self.size == 0:
            raise IndexError
        
        top_element = self.stack.pop()
        cur_minimum = top_element[self.MINIMUM]
        self.stack.append(top_element)

        return cur_minimum
    
    def get_size(self) -> int:
        return self.size
    
    def is_empty(self):
        return self.size == 0
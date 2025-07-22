from data_structures.fundamentals.deque_minimum_stack import MinimumStack

class MinimumQueue:
    ELEMENT_INDEX = 0
    MINIMUM_INDEX = 1

    def __init__(self): 
        self.push_stack = MinimumStack()
        self.serve_stack = MinimumStack()
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, element):
        self.push_stack.push(element)
        self.size += 1
    
    def serve(self):
        if self.size == 0:
            raise IndexError
        
        if not self.serve_stack.is_empty(): 
            self.size -= 1
            return self.serve_stack.pop()

        while not self.push_stack.is_empty():
            self.serve_stack.push(self.push_stack.pop())

        self.size -= 1

        return self.serve_stack.pop()

    def get_minimum(self):
        if self.size == 0:
            raise IndexError
        
        if self.push_stack.is_empty():
            return self.serve_stack.get_minimum()
        elif self.serve_stack.is_empty():
            return self.push_stack.get_minimum()

        return min(self.push_stack.get_minimum(), self.serve_stack.get_minimum())
    

if __name__ == '__main__':
    min_queue = MinimumQueue()

    min_queue.push(1)
    min_queue.push(3)
    min_queue.push(-1)
    min_queue.push(5)
    min_queue.push(9)

    print(min_queue.get_minimum())

    print(min_queue.serve())

    print(min_queue.get_minimum())
    
    min_queue.serve()
    min_queue.serve()

    print(min_queue.get_minimum())



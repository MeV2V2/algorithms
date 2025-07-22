import unittest
from collections import deque

from data_structures.fundamentals.deque_minimum_stack import MinimumStack

class TestMinimumStack(unittest.TestCase):

    def test_push_and_size(self):
        stack = MinimumStack()
        stack.push(10)
        stack.push(20)
        self.assertEqual(stack.get_size(), 2)

    def test_peek(self):
        stack = MinimumStack()
        stack.push(5)
        self.assertEqual(stack.peek(), 5)
        self.assertEqual(stack.get_size(), 1)

    def test_get_minimum_basic(self):
        stack = MinimumStack()
        stack.push(5)
        stack.push(3)
        stack.push(7)
        self.assertEqual(stack.get_minimum(), 3)

    def test_get_minimum_after_pop(self):
        stack = MinimumStack()
        stack.push(4)
        stack.push(2)
        stack.push(5)
        self.assertEqual(stack.get_minimum(), 2)
        stack.pop()
        self.assertEqual(stack.get_minimum(), 2)
        stack.pop()
        self.assertEqual(stack.get_minimum(), 4)

    def test_pop(self):
        stack = MinimumStack()
        stack.push(1)
        stack.push(2)
        popped = stack.pop()
        self.assertEqual(popped, 2)
        self.assertEqual(stack.get_size(), 1)

    def test_empty_pop_raises(self):
        stack = MinimumStack()
        with self.assertRaises(IndexError):
            stack.pop()

    def test_empty_peek_raises(self):
        stack = MinimumStack()
        with self.assertRaises(IndexError):
            stack.peek()

    def test_empty_minimum_raises(self):
        stack = MinimumStack()
        with self.assertRaises(IndexError):
            stack.get_minimum()

    def test_sequence_of_operations(self):
        stack = MinimumStack()
        stack.push(3)
        stack.push(1)
        self.assertEqual(stack.get_minimum(), 1)
        self.assertEqual(stack.peek(), 1)
        stack.pop()
        self.assertEqual(stack.get_minimum(), 3)
        stack.push(0)
        self.assertEqual(stack.get_minimum(), 0)


if __name__ == '__main__':
    unittest.main()

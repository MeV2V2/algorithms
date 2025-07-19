import unittest
from data_structures.fundamentals.minimum_stack import MinimumStack

class TestMinimumStack(unittest.TestCase):
    def setUp(self):
        self.stack = MinimumStack()

    def test_push_and_peek(self):
        self.stack.push(5)
        self.assertEqual(self.stack.peek(), 5)
        self.assertEqual(self.stack.get_minimum(), 5)
        self.assertEqual(self.stack.get_size(), 1)

        self.stack.push(3)
        self.assertEqual(self.stack.peek(), 3)
        self.assertEqual(self.stack.get_minimum(), 3)
        self.assertEqual(self.stack.get_size(), 2)

        self.stack.push(7)
        self.assertEqual(self.stack.peek(), 7)
        self.assertEqual(self.stack.get_minimum(), 3)
        self.assertEqual(self.stack.get_size(), 3)

    def test_pop(self):
        self.stack.push(10)
        self.stack.push(5)
        self.stack.push(15)

        self.assertEqual(self.stack.pop(), 15)
        self.assertEqual(self.stack.get_minimum(), 5)
        self.assertEqual(self.stack.get_size(), 2)

        self.assertEqual(self.stack.pop(), 5)
        self.assertEqual(self.stack.get_minimum(), 10)
        self.assertEqual(self.stack.get_size(), 1)

        self.assertEqual(self.stack.pop(), 10)
        self.assertEqual(self.stack.get_size(), 0)

    def test_peek_empty_stack(self):
        with self.assertRaises(IndexError):
            self.stack.peek()

    def test_pop_empty_stack(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_get_minimum_empty_stack(self):
        with self.assertRaises(IndexError):
            self.stack.get_minimum()

    def test_mixed_operations(self):
        values = [9, 4, 6, 2, 10]
        mins = [9, 4, 4, 2, 2]
        for val, expected_min in zip(values, mins):
            self.stack.push(val)
            self.assertEqual(self.stack.get_minimum(), expected_min)

        self.assertEqual(self.stack.pop(), 10)
        self.assertEqual(self.stack.get_minimum(), 2)

        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.get_minimum(), 4)

        self.stack.push(1)
        self.assertEqual(self.stack.get_minimum(), 1)

if __name__ == '__main__':
    unittest.main()

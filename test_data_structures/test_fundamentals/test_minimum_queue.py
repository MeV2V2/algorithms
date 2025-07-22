import unittest
from data_structures.fundamentals.minimum_queue import MinimumQueue

class TestMinimumQueue(unittest.TestCase):

    def test_push_and_serve_order(self):
        q = MinimumQueue()
        q.push(1)
        q.push(2)
        q.push(3)
        self.assertEqual(q.serve(), 1)
        self.assertEqual(q.serve(), 2)
        self.assertEqual(q.serve(), 3)

    def test_get_minimum_basic(self):
        q = MinimumQueue()
        q.push(3)
        q.push(1)
        q.push(2)
        self.assertEqual(q.get_minimum(), 1)
        q.serve()  # Removes 3
        self.assertEqual(q.get_minimum(), 1)
        q.serve()  # Removes 1
        self.assertEqual(q.get_minimum(), 2)

    def test_get_minimum_single_element(self):
        q = MinimumQueue()
        q.push(42)
        self.assertEqual(q.get_minimum(), 42)

    def test_len_and_is_empty(self):
        q = MinimumQueue()
        self.assertEqual(len(q), 0)
        q.push(5)
        self.assertEqual(len(q), 1)
        q.push(3)
        self.assertEqual(len(q), 2)
        q.serve()
        self.assertEqual(len(q), 1)
        q.serve()
        self.assertEqual(len(q), 0)

    def test_interleaved_operations(self):
        q = MinimumQueue()
        q.push(5)
        q.push(2)
        self.assertEqual(q.get_minimum(), 2)
        q.serve()  # Pops 5
        self.assertEqual(q.get_minimum(), 2)
        q.push(1)
        self.assertEqual(q.get_minimum(), 1)
        q.serve()  # Pops 2
        self.assertEqual(q.get_minimum(), 1)
        q.serve()  # Pops 1
        self.assertEqual(len(q), 0)

    def test_serve_empty(self):
        q = MinimumQueue()
        with self.assertRaises(IndexError):
            q.serve()

    def test_get_minimum_empty(self):
        q = MinimumQueue()
        with self.assertRaises(IndexError):
            q.get_minimum()

if __name__ == '__main__':
    unittest.main()

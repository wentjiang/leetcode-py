import unittest
import question_88

solution = question_88.Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution.merge(self, [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)

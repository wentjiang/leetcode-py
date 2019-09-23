import unittest

from question_70 import Solution

solution = Solution()

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(3, solution.climbStairs(3))

    def test_something_1(self):
        self.assertEqual(5, solution.climbStairs(4))

    def test_something_2(self):
        self.assertEqual(8, solution.climbStairs(5))
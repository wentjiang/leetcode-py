import unittest

from solution.q101_200.question_136 import Solution
from solution.q101_200.question_136 import Solution1

solution = Solution()
solution1 = Solution1()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1, solution.singleNumber([2, 2, 1]))

    def test_something_1(self):
        self.assertEqual(4, solution.singleNumber([4, 1, 2, 1, 2]))

    def test_something_2(self):
        self.assertEqual(1, solution1.singleNumber([2, 2, 1]))

    def test_something_3(self):
        self.assertEqual(4, solution1.singleNumber([4, 1, 2, 1, 2]))

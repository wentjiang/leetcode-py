import unittest

from solution.q101_200 import question_119

solution = question_119.Solution()


class question_119_test(unittest.TestCase):
    def test_getRow_1(self):
        self.assertEquals([1, 3, 3, 1], solution.getRow(3))

    def test_getRow_2(self):
        self.assertEquals([1], solution.getRow(0))

    def test_getRow_3(self):
        self.assertEquals([1, 1], solution.getRow(1))

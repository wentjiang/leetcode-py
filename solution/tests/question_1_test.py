import unittest

from solution.q1_100 import question_1

solution = question_1.Solution()


class question_1_test(unittest.TestCase):

    def test_twoSum_1(self):
        self.assertEqual([0, 1], solution.twoSum([2, 7, 11, 15], 9))

    def test_twoSum_2(self):
        self.assertEqual([1, 2], solution.twoSum([3, 2, 4], 6))


if __name__ == '__main__':
    unittest.main()

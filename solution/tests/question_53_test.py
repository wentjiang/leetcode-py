import unittest

from solution.q1_100 import question_53

solution = question_53.Solution
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(6, solution.maxSubArray(solution, [-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    def test_something1(self):
        self.assertEqual(3, solution.maxSubArray(solution, [1,2]))

if __name__ == '__main__':
    unittest.main()

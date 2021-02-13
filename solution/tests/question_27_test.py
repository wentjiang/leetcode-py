import unittest

from solution.q1_100 import question_27

solution = question_27.Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(5, solution.removeElement(solution, [0, 1, 2, 2, 3, 0, 4, 2], 2))
        self.assertEqual(5, solution.removeElement1(solution, [0, 1, 2, 2, 3, 0, 4, 2], 2))


if __name__ == '__main__':
    unittest.main()

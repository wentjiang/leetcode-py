import unittest

import question_69

solution = question_69.Solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(2,solution.mySqrt(self,4))

    def test_something1(self):
        self.assertEqual(2, solution.mySqrt(self, 8))

    def test_something2(self):
        self.assertEqual(1, solution.mySqrt(self, 1))

    def test_something3(self):
        self.assertEqual(0, solution.mySqrt(self, 0))

    def test_something4(self):
        self.assertEqual(3, solution.mySqrt(self, 9))

    def test_something5(self):
        self.assertEqual(1, solution.mySqrt(self, 2))

    def test_something6(self):
        self.assertEqual(2, solution.mySqrt(self, 5))

if __name__ == '__main__':
    unittest.main()

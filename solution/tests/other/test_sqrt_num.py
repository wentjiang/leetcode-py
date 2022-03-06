from unittest import TestCase

from solution.other.sqrt_num import sqrt_num
import math


class Test(TestCase):
    def test_sqrt_num(self):
        self.assertEqual(1, sqrt_num(num=1))

    def test_sqrt_num_1(self):
        self.assertTrue(abs(sqrt_num(num=4) - math.sqrt(4)) < 0.01)

    def test_sqrt_num_2(self):
        print(math.sqrt(3485734897))
        self.assertTrue(abs(sqrt_num(num=3485734897) - math.sqrt(3485734897)) < 0.01)

from unittest import TestCase

import math

from solution.other.sqrt_num_2 import cal_sqrt


class Test(TestCase):
    def test_sqrt_num(self):
        self.assertEqual(1, cal_sqrt(num=1))

    def test_sqrt_num_1(self):
        self.assertTrue(abs(cal_sqrt(num=4) - math.sqrt(4)) < 0.01)

    def test_sqrt_num_2(self):
        print(math.sqrt(3485734897))
        self.assertTrue(abs(cal_sqrt(num=3485734897) - math.sqrt(3485734897)) < 0.01)

from unittest import TestCase
from solution.q501_600 import question_521

solution = question_521.Solution()


class TestSolution(TestCase):
    def test_find_luslength(self):
        self.assertEqual(3, solution.findLUSlength("aba", "cdc"))

    def test_find_luslength_1(self):
        self.assertEqual(1, solution.findLUSlength("a", "c"))

    def test_find_luslength_2(self):
        self.assertEqual(3, solution.findLUSlength("aaa", "bbb"))

    def test_find_luslength_3(self):
        self.assertEqual(-1, solution.findLUSlength("aaa", "aaa"))

    def test_find_luslength_4(self):
        self.assertEqual(17, solution.findLUSlength("aefawfawfawfaw", "aefawfeawfwafwaef"))

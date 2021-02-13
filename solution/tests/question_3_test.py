import unittest

from solution.q1_100 import question_3

solution = question_3.Solution()


class question_3_test(unittest.TestCase):

    def test_lengthOfLongestSubstring_1(self):
        self.assertEqual(5, solution.lengthOfLongestSubstring('tmmzuxt'))

    def test_lengthOfLongestSubstring_2(self):
        self.assertEqual(3, solution.lengthOfLongestSubstring('abcabcbb'))

    def test_lengthOfLongestSubstring_3(self):
        self.assertEqual(3, solution.lengthOfLongestSubstring('pwwkew'))

    def test_lengthOfLongestSubstring_4(self):
        self.assertEqual(1, solution.lengthOfLongestSubstring(' '))

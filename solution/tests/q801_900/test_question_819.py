from unittest import TestCase
from solution.q801_900 import question_819

solution = question_819.Solution()


class TestSolution(TestCase):

    def test_mostCommonWord(self):
        self.assertEqual("ball",
                         solution.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))

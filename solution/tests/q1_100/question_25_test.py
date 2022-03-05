import unittest

from solution.q1_100 import question_25

solution = question_25.Solution()

class question_25_test(unittest.TestCase):

    def reverseKGroup(self):
       listNode = solution.reverseKGroup()
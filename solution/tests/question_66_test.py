from unittest import TestCase
import question_66
solution = question_66.Solution();

class question_66_test(TestCase):
    def test_plusOne(self):
        self.assertEqual([1,2,4], solution.plusOne([1,2,3]))
    def test_plusOne_1(self):
        self.assertEqual([4,3,2,2], solution.plusOne([4,3,2,1]))

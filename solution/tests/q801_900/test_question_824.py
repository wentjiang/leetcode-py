from unittest import TestCase
from solution.q801_900 import question_824

solution = question_824.Solution()


class TestSolution(TestCase):

    def test_toGoatLatin(self):
        self.assertEqual("Imaa peaksmaaa oatGmaaaa atinLmaaaaa",
                         solution.toGoatLatin("I speak Goat Latin"))

    def test_toGoatLatin1(self):
        self.assertEqual(
            "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa",
            solution.toGoatLatin("The quick brown fox jumped over the lazy dog"))

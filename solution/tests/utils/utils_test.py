import unittest
import utils.utils


class utils_test(unittest.TestCase):

    def test(self):
        listNode = utils.utils.getListNode([1, 2, 3, 4, 5])
        self.assertEqual('1 2 3 4 5 ', utils.utils.printListNode(listNode))

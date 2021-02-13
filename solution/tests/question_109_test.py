import os
import sys

dir_mytest = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, dir_mytest)
import unittest
from solution.utils.utils import getListNode, getTreeNodeArrayList
from solution.q101_200 import question_109

solution = question_109.Solution


class question_109_test(unittest.TestCase):
    def test_something(self):
        listNode = getListNode([-10, -3, 0, 5, 9])
        treeNode = solution.sortedListToBST(self, head=listNode)
        array = getTreeNodeArrayList(treeNode)
        print(array)

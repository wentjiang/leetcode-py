# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import floor

from solution.utils.utils import ListNode, TreeNode


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        array = []
        while head is not None:
            array.append(head.val)
            head = head.next
        return buildTree(array, 0, len(array))


def buildTree(array, start, end) -> TreeNode:
    if start == end:
        return TreeNode(array[start])
    middle_index = floor((start + end) / 2)
    treeNode = TreeNode(array[middle_index], buildTree(array, start, middle_index), buildTree(array, middle_index, end))
    return treeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from solution.utils.utils import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        is_balanced = get_balance_height(root)
        return is_balanced[0]


def get_balance_height(root: TreeNode):
    if root is None:
        return True, 0
    is_left_balance, left_height = get_balance_height(root.left)
    is_right_balance, right_height = get_balance_height(root.right)
    return is_left_balance and is_right_balance \
           and abs(left_height - right_height) <= 1 \
        , max(left_height, right_height) + 1

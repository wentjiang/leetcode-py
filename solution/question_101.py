# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return symmetric(root.left, root.right)


def symmetric(p, q):
    if p is None and q is None:
        return True
    if (p is None and q) or (p and q is None) or p.val != q.val:
        return False
    if not symmetric(p.left, q.right):
        return False
    if not symmetric(p.right, q.left):
        return False
    return True



from utils.utils import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return same(p, q)


def same(p, q):
    if p is None and q is None:
        return True
    if (p is None and q) or (p and q is None) or p.val != q.val:
        return False
    if not same(p.left, q.left):
        return False
    if not same(p.right, q.right):
        return False
    return True

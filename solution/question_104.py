# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return getMaxDepth(0, root, 0)


def getMaxDepth(layer, root, maxLayer):
    if root != None:
        if maxLayer < layer:
            maxLayer = layer
        return max(getMaxDepth(layer + 1, root.left, maxLayer), getMaxDepth(layer + 1, root.right, maxLayer))
    else:
        return layer

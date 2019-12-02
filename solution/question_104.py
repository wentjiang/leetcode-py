# Definition for a binary tree node.
from utils.utils import TreeNode


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

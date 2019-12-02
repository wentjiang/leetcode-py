from typing import List

from utils.utils import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def viewTree(root):
            result = []
            if root is None:
                return result
            if root.left is not None:
                result = result + viewTree(root.left)
            result += [root.val]
            if root.right is not None:
                result = result + viewTree(root.right)
            return result

        result = viewTree(root)
        return result

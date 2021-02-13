from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def getListNode(nums: List[int]) -> ListNode:
    prehead = ListNode(0)
    oriPreHead = prehead
    for i in nums:
        node = ListNode(i)
        prehead.next = node
        prehead = prehead.next
    return oriPreHead.next


def printListNode(listNode: ListNode) -> str:
    result = ''
    while listNode is not None:
        result += str(listNode.val) + ' '
        listNode = listNode.next
    return result

def getTreeNodeArrayList(treeNode: TreeNode):
    if treeNode is None:
        return []
    array = [treeNode.val]
    if treeNode.left is not None:
        left_array = getTreeNodeArrayList(treeNode.left)
        array.extend(left_array)
    if treeNode.right is not None:
        right_array = getTreeNodeArrayList(treeNode.right)
        array.extend(right_array)
    return array

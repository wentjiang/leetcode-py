# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(0)
        temp = []
        for i in lists:
            while i:
                temp.append(i.val)
                i = i.next

        temp.sort()
        temp_node = head
        for i in temp:
            temp_node.next = ListNode(i)
            temp_node = temp_node.next
        return head.next

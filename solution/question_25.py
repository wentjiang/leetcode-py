# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 0:
            return head
        first = ListNode(0)
        first.next = head
        last = ListNode(0)
        final_last = head
        last.next = final_last
        cur = head
        for i in range(k):
            first.next = cur.next
            cur.next = last.next
            last.next = cur.next
            cur = first.next
        final_last.next = cur
        return last.next
    #todo


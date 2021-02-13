# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        first = ListNode(None)
        first.next = head
        pre = head
        pre_next = head.next
        while pre.next and pre_next:
            if pre.val == pre_next.val:
                pre.next = pre_next.next
                if pre_next:
                    pre_next = pre_next.next
            else:
                pre = pre.next
                pre_next = pre_next.next
        return first.next

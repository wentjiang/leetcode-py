# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        hash_table = {}
        while head.next != None:
            if hash_table.get(head) == None:
                hash_table[head] = head.next
                head = head.next
            else:
                return True
        return False

class Solution1:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        head1 = head
        head2 = head
        while head1 != None and head2 != None:
            head1 = head1.next
            if head2.next != None:
                head2 = head2.next.next
            else:
                return False
            if head1 == head2:
                return True
        return False
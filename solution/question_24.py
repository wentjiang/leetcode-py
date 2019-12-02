# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        orgHead = head.next

        #已经交换的尾节点记录
        tail = head
        while head is not None and head.next is not None:
            #将尾节点的下一个指向后边的下一个
            tail.next = head.next
            #进行交换
            temp = head.next
            head.next = temp.next
            temp.next = head
            #设置新的尾节点
            tail = head
            head = head.next
        if head is not None:
            tail.next = head
        return orgHead

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head
        resultHead = head
        # 已经交换的尾节点记录
        first = True
        # 上一个倒置顺序的结尾,也就是下一个倒置顺序头的前一个元素
        prehead = None
        while head is not None:
            #当前组需要转换的数目
            inverseNum = None
            # 先确定当前组交换的个数 <= k
            for i in range(k):
                if head.next is not None:
                    inverseNum = i + 1
                else:
                    break
            # 组内倒转
            tail = head.next
            for i in range(inverseNum):
                if i == inverseNum - 1 :
                    if first:
                        resultHead = tail
                        first = False
                    prehead = tail
                #获取最后元素的下一个元素的引用
                temp = tail.next
                #最后元素下一个引用连接head
                tail.next = head
                #将head转换为tail
                head = tail
                #tail转换为tail.next,变为下一个元素
                tail = temp
            prehead.next = head
        return resultHead

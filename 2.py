# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, t=0) -> ListNode:
        ret = ListNode(t + l1.val + l2.val)
        t = ret.val // 10
        if l1.next or l2.next or t:
            if l1.next is None:
                l1.next = ListNode(0)
            if l2.next is None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next, l2.next, t)
        ret.val -= t * 10
        return ret

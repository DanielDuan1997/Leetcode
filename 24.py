# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p1, p2 = head, head.next
        while True:
            p1.next = p2.next
            p2.next = p1
            if p1 == head:
                head = p2
            if p1.next and p1.next.next:
                tmp = p1.next
                p1.next = tmp.next
                p1 = tmp
                p2 = p1.next
            else:
                break
        return head

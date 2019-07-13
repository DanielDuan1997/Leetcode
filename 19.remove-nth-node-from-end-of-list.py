#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return None
        dummy = ListNode(None)
        dummy.next = head
        p = dummy
        q = p
        for i in range(n):
            q = q.next
        while q and q.next:
            p = p.next
            q = q.next
        p.next = p.next.next
        return dummy.next


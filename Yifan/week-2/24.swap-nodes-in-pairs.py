#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head
        new_head = head.next
        p = head
        p.next = p.next.next
        new_head.next = head

        while p and p.next and p.next.next:
            q = p.next
            p.next = p.next.next
            q.next = q.next.next
            p.next.next = q
            p = q
        return new_head
        


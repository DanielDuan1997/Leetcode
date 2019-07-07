#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l1
        carry = 0
        while True:
            temp = (l1.val+l2.val)+carry
            carry = temp//10
            l1.val = temp % 10
            if not l1.next:
                l1.next = l2.next
                break
            if not l2.next:
                break
            l1, l2 = l1.next, l2.next

        while True:
            if not l1.next:
                break
            l1 = l1.next
            l1.val += carry
            carry = 0
            if l1.val == 10:
                l1.val = l1.val-10
                carry = 1

        if carry:
            l1.next = ListNode(1)
        return head

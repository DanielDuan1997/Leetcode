"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        p0 = head
        head1 = Node(p0.val, p0.next, p0.random)
        p1 = head1
        p0.copy = p1
        while p0.next:
            p0 = p0.next
            p1.next = Node(p0.val, p0.next, p0.random)
            p1 = p1.next
            p0.copy = p1
        p0 = head
        p1 = head1
        while p0 is not None:
            if p0.random is not None:
                p1.random = p0.random.copy
            p0 = p0.next
            p1 = p1.next
        return head1

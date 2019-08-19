"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from queue import Queue
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = Queue()
        q.put(root)
        while not q.empty():
            len_q = len(q.queue)
            for i in range(len_q):
                node = q.get()
                if i == len_q - 1:
                    node.next = None
                else:
                    node.next = q.queue[0]
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
        return root

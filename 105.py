# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        pos = dict()
        for (index, val) in enumerate(inorder):
            pos[val] = index
        x = 0
        def dfs(le, ri):
            if le > ri:
                return None
            nonlocal pos
            nonlocal x
            p = pos[preorder[x]]
            node = TreeNode(preorder[x])
            x += 1
            node.left = dfs(le, p-1)
            node.right = dfs(p+1, ri)
            return node
        return dfs(0, len(inorder)-1)

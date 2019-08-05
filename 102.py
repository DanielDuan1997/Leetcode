# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ret = []
        def dfs(x, depth):
            if depth == len(ret):
                ret.append([])
            ret[depth].append(x.val)
            if x.left:
                dfs(x.left, depth + 1)
            if x.right:
                dfs(x.right, depth + 1)
        dfs(root, 0)
        return ret

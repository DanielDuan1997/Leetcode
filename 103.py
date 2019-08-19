# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        level = [root]
        ret = []
        flag = True
        while len(level):
            level.reverse()
            ret.append([node.val for node in level])
            if flag:
                level= [child for node in level for child in (node.left, node.right) if child]
            else:
                level = [child for node in level for child in (node.right, node.left) if child]
            flag = not flag
        return ret

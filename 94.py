class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ret = []
        def dfs(x):
            if x.left:
                dfs(x.left)
            ret.append(x.val)
            if x.right:
                dfs(x.right)
        dfs(root)
        return ret

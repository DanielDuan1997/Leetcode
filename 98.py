class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        flag = True
        def dfs(x):
            nonlocal flag
            if not flag:
                return [0, 0]
            ret = [x.val, x.val]
            if x.left:
                left_info = dfs(x.left)
                if left_info[1] >= x.val:
                    flag = False
                ret[0] = left_info[0]
            if x.right:
                right_info = dfs(x.right)
                if right_info[0] <= x.val:
                    flag = False
                ret[1] = right_info[1]
            return ret
        dfs(root)
        return flag

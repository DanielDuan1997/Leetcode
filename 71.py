from collections import deque
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        stack = deque()
        for name in path:
            if len(name) == 0 or name == ".": continue
            if name == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(name)
        ret = "/" + "/".join(stack)
        return ret

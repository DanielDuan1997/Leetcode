class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = []
        for ch in s:
            if ch == '(':
                a.append(0)
            elif ch == ')':
                a.append(5)
            elif ch == '[':
                a.append(1)
            elif ch ==']':
                a.append(4)
            elif ch == '{':
                a.append(2)
            else:
                a.append(3)
        stack = []
        for i in range(len(a)):
            if a[i] <= 2:
                stack.append(a[i])
            else:
                if len(stack) == 0 or stack[-1] + a[i] != 5:
                    return False
                stack.pop()
        return len(stack) == 0

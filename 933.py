from collections import deque
class RecentCounter(object):

    def __init__(self):
        self.que = deque()
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        while len(self.que) > 0 and t - self.que[0] > 3000:
            self.que.popleft()
        self.que.append(t)
        return len(self.que)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

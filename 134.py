class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tot, cur_sum = 0, 0
        start = 0
        for i in range(len(gas)):
            tot += gas[i] - cost[i]
            cur_sum += gas[i] - cost[i]
            if cur_sum < 0:
                cur_sum = 0
                start = i + 1
        if tot < 0:
            return -1
        else:
            return start

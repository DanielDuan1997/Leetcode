import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)
        if n == 0 or m == 0:
            return []
        heap = []
        ind = [0] * n
        for i in range(n):
            heapq.heappush(heap, (nums1[i] + nums2[ind[i]], i))
        ans = []
        while k > 0 and n > 0:
            x = heap[0][1]
            ans.append([nums1[x], nums2[ind[x]]])
            heapq.heappop(heap)
            ind[x] += 1
            if ind[x] < m:
                heapq.heappush(heap, (nums1[x] + nums2[ind[x]], x))
            else:
                n -= 1
            k -= 1
        return ans

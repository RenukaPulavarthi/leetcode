import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = Counter(nums)
        heap = [(-dict[i], i) for i in dict]
        heapq.heapify(heap)
        ans = []
        while k > 0 and len(heap) > 0:
            curr = heapq.heappop(heap)
            ans.append(curr[1])
            k -= 1
        return ans

from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = [[-freq[i], i] for i in freq]
        heapq.heapify(heap)
        ans = []
        print(heap)
        while k:
            ele = heap[0][1]
            heapq.heappop(heap)
            ans.append(ele)
            k -= 1
        return ans
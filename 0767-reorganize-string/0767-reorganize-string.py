from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        heap = [(-freq[i], i) for i in freq]
        heapq.heapify(heap)
        ans = ""
        prev = None
        while len(heap) > 0:
            print(heap, prev, ans)
            k = heapq.heappop(heap)
            if len(ans) > 0 and k[1] == ans[-1]:
                return ""
            ans += k[1]
            if prev is not None:
                heapq.heappush(heap, prev)
            if k[0] < -1:
                prev = (k[0] + 1, k[1])
            else:
                prev = None
        if prev is not None and prev[1] == ans[-1]:
            return ""
        return ans
            


        
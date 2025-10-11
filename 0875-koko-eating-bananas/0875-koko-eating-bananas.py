import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 0, max(piles)
        ans = 0

        def possible(idx):
            hrs = 0
            for i in piles:
                hrs += math.ceil(i / idx)
            return hrs <= h

        while low <= high:
            mid = low + (high - low) // 2
            if possible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
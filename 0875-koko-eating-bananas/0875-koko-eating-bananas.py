import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        def solve(idx):
            curr = 0
            for i in piles:
                curr += math.ceil(i / idx)
            return curr <= h

        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            if solve(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
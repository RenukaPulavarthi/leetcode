class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        ans = 0
        if cost1 + cost2 > costBoth:
            ans = min(need1, need2)
            need1 -= ans
            need2 -= ans
            ans = (ans * costBoth)
            if need1 > 0:
                if cost1 > costBoth:
                    ans += (need1 * costBoth)
                else:
                    ans += (need1 * cost1)
            if need2 > 0:
                if cost2 > costBoth:
                    ans += (need2 * costBoth)
                else:
                    ans += (need2 * cost2)
        else:
            ans += (need1 * cost1)
            ans += (need2 * cost2)
        return ans

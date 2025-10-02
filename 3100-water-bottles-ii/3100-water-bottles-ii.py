class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            ans += 1
            numBottles -= numExchange
            numBottles += 1
            numExchange += 1
            # print(numBottles)
        return ans
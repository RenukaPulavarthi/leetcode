class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        ans = 0
        for i in prices[1::]:
            ans = max(ans, i - mini)
            mini = min(mini, i)
        return ans

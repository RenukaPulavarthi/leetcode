class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)
        pre = [ prices[-1] ]
        for i in range(n-2, -1, -1):
            pre.append(max(pre[-1], prices[i]))
        pre = pre[::-1]
        # print(pre)
        for i in range(n):
            ans = max(ans, pre[i] - prices[i])
        return ans

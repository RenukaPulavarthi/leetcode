class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = [float('inf')]

        def solve(idx, curr, coin):
            if curr == amount:
                ans[0] = min(ans[0], coin)
                return
            if idx >= len(coins) or curr > amount:
                return
            solve(idx, curr + coins[idx], coin + 1)
            solve(idx + 1, curr, coin)

        solve(0, 0, 0)
        return ans[0] if ans[0] != float('inf') else -1

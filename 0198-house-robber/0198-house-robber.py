class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)

        def solve(idx):
            if idx >= n:
                return 0
            if idx in dp:
                return dp[idx]
            k = 0
            for i in range(idx + 2, n):
                k = max(k, solve(i))
            dp[idx] = k + nums[idx]
            return k + nums[idx]
        
        return max(solve(0), solve(1))

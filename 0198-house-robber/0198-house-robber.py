class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def solve(idx):
            if idx >= len(nums):
                return 0
            if idx in dp:
                return dp[idx]
            maxi = 0
            for i in range(idx,len(nums)):
                maxi=max(maxi, solve(i+2))
            dp[idx] = nums[idx] + maxi
            return nums[idx] + maxi
        
        return max(solve(0), solve(1))
        
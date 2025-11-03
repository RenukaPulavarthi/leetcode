class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        ans = 0
        n = len(nums)
        for i in range(n):
            curr += nums[i]
            ans = max(ans, curr)
            if curr < 0:
                curr = 0
        return ans
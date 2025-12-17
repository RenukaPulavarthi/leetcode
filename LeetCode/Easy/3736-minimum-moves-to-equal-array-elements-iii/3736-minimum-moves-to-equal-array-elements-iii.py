class Solution:
    def minMoves(self, nums: List[int]) -> int:
        k = max(nums)
        ans = 0
        for i in nums:
            ans += (k - i)
        return ans
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        lst = [nums[0] * nums[1], nums[-1] * nums[-2], nums[0] * nums[-1]]
        ans = 0
        for k in lst:
            if k < 0:
                k *= (-100000)
            else:
                k *= 100000
            ans = max(ans, k)
        return ans   
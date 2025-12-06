from collections import Counter
class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        if k == 0:
            return len(nums)
        nums.sort()
        cutoff = nums[len(nums) - k]
        ans = 0
        for i in nums:
            if i < cutoff:
                ans += 1
        return ans
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_point = 0
        for i in range(len(nums)):
            if i > max_point:
                return False
            if i + nums[i] > max_point:
                max_point = i + nums[i]
        return True

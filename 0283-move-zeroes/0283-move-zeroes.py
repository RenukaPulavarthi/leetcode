class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        idx = 0
        for i in nums:
            if i != 0:
                nums[idx] = i
                idx += 1
        while idx < len(nums):
            nums[idx] = 0
            idx += 1
            


        
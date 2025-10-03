class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero = 0
        pro = 1
        for i in nums:
            if i == 0:
                zero += 1
            else:
                pro *= i
        for i in range(len(nums)):
            if zero > 1:
                nums[i] = 0
            elif zero == 1 and nums[i] != 0:
                nums[i] = 0
            else:
                if nums[i] == 0:
                    nums[i] = pro
                else:
                    nums[i] = (pro // nums[i])
        return nums
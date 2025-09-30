class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            curr = []
            for i in range(len(nums)-1):
                curr.append((nums[i] + nums[i+1]) % 10)
            nums=[i for i in curr]
        return nums[0]
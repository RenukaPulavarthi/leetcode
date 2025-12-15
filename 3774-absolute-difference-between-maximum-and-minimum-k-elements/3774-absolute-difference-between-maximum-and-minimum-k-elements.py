class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        # print(nums[len(nums)-k::])
        return abs(sum(nums[len(nums)-k::]) - sum(nums[:k]))
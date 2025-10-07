class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums = [[nums[i], i] for i in range(n)]
        nums.sort()
        low, high = 0, n - 1
        while low < high:
            if nums[low][0] + nums[high][0] == target:
                return [nums[low][1], nums[high][1]]
            elif nums[low][0] + nums[high][0] > target:
                high -= 1
            else:
                low += 1
        return []
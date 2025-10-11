class Solution:
    def rob(self, nums: List[int]) -> int:
        max_pro = []
        n = len(nums)
        for i in range(n):
            if i == 0:
                max_pro.append(nums[0])
            elif i == 1:
                max_pro.append(nums[1])
            else:
                max_pro.append(max(nums[i] + max_pro[-2], max_pro[-1]))
        return max_pro[-1]
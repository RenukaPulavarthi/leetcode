class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            d[i] = 1
        ans = []
        for i in range(min(nums), max(nums) + 1):
            if i not in d:
                ans.append(i)
        return ans
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        d = {}
        ans = float('inf')
        for i in range(len(nums) - 1, -1, -1):
            rev = int(str(nums[i])[::-1])
            if rev in d:
                ans = min(ans, d[rev] - i)
            d[nums[i]] = i
        return ans if ans != float('inf') else -1
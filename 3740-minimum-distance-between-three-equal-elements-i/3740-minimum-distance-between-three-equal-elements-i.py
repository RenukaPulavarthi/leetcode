class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        ans = float('inf')
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] == nums[j] == nums[k]:
                        ans = min(ans, abs(i-j) + abs(j-k) + abs(k-i))
        return ans if ans != float('inf') else -1
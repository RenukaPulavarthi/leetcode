class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        low, high = 0, n-1
        ans = 0
        while low < high:
            ans = max(ans, min(height[low], height[high]) * (high - low))
            if height[low] <= height[high]:
                low += 1
            else:
                high -= 1
        return ans
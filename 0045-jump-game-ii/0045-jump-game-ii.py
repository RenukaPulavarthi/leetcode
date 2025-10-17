class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, 0 
        ans = 0
        while right < n - 1:
            maxi = left
            for i in range(left, right + 1):
                maxi = max(maxi, i + nums[i])
            left = right + 1
            right = maxi
            ans +=1
        return ans


    
class Solution:
    def jump(self, nums: List[int]) -> int:
        cnt = 0
        left, right = 0, 0
        while right < len(nums) - 1:
            maxi = 0
            for i in range(left, right+1):
                maxi = max(maxi, i+nums[i])
            left = right + 1
            right = maxi
            cnt += 1
        return cnt
            
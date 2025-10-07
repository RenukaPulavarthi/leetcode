class Solution:
    def trap(self, nums: List[int]) -> int:
        pre = [nums[0]]
        n = len(nums)
        for i in range(1,n):
            pre.append(max(pre[-1], nums[i]))
        post = [nums[-1]]
        for i in range(n - 2, -1, -1):
            post.append(max(post[-1], nums[i]))
        post = post[::-1]
        ans = 0
        for i in range(n):
            ans += (min(pre[i], post[i]) - nums[i])
        return ans

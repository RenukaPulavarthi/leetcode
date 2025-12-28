class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        pre = [nums[0]]
        suf = []
        for i in nums[1::]:
            pre.append(pre[-1] + i)
        suf = [nums[-1]]
        for i in nums[:len(nums)-1:][::-1]:
            # print(i)
            suf.append(min(suf[-1], i))
        suf = suf[::-1]
        ans = pre[0] - suf[1]
        # print(pre, suf)
        for i in range(len(pre)-1):
            ans = max(ans, pre[i] - suf[i + 1])

        return ans

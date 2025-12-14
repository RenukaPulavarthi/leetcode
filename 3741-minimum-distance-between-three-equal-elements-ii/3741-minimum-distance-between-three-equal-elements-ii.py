class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        ans = float('inf')
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = []
            d[nums[i]].append(i)
            if len(d[nums[i]]) == 3:
                k, l, m = d[nums[i]]
                ans = min(ans, l - k + m - l + m - k)
                d[nums[i]].pop(0)
                # print(d)
        return ans if ans != float('inf') else -1
                
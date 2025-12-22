from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        d = Counter(nums)
        n = len(nums)
        cnt = 0
        for i in d:
            if d[i] > 1:
                cnt += 1
        idx = 0
        while cnt != 0:
            z = [idx, idx + 1, idx + 2]
            for i in z:
                if i >= n:
                    break
                d[nums[i]] -= 1
                if d[nums[i]] == 1:
                    cnt -= 1
            ans += 1
            idx = idx + 3
        return ans



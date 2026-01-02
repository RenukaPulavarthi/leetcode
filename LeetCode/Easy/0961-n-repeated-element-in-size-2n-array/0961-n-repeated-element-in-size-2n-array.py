from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = Counter(nums)
        for i in d:
            if d[i] > 1:
                return i
        return -1
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        n = len(nums)
        for i in freq:
            if freq[i] > n // 2:
                return i
        return -1
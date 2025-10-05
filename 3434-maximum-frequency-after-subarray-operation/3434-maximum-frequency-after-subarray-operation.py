from collections import Counter
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        
        def get(ele):
            ans = curr = 0
            for i in nums:
                if i == k:
                    curr -= 1
                if i == ele:
                    curr += 1
                if curr < 0:
                    curr += 1
                ans = max(ans, curr)
            return ans
        
        ans = max(get(i) for i in freq)
        return freq[k] + ans
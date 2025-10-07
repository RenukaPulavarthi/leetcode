class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        n = len(s)
        d = {}
        ans = 0
        for end in range(n):
            if s[end] in d and d[s[end]] >= start:
                start = d[s[end]] + 1
            d[s[end]] = end
            ans = max(ans, end - start + 1)
            # print(start, end)
        return ans

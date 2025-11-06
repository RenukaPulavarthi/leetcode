class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        d = {}
        ans = 0
        st = 0
        for i in range(n):
            if s[i] in d and st <= d[s[i]]:
                st = d[s[i]] + 1
            d[s[i]] = i
            ans = max(ans, i - st + 1)
        return ans
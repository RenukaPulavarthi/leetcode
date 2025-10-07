class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = {}
        n = len(s)
        ans = [-1,-1]
        for i in range(n):
            start = 0
            end = i
            while end < n:
                if start == end and s[start] == s[end]:
                    dp[(start, end)] = 1
                    ans[0], ans[1] = start, end
                elif start + 1 == end and s[start] == s[end]:
                    dp[(start, end)] = 1
                    ans[0], ans[1] = start, end
                elif s[start] == s[end] and (start + 1, end - 1) in dp:
                    dp[(start, end)] = 1
                    ans[0], ans[1] = start, end
                start += 1
                end += 1
        return s[ans[0] : ans[1] + 1]
            

class Solution:
    def lexSmallest(self, s: str) -> str:
        n = len(s)
        ans = s
        for i in range(1, n+1):
            curr = s[:i][::-1] + s[i::]
            ans = min(ans, curr)
            curr = s[:i] + s[i::][::-1]
            ans = min(ans, curr)
        return ans



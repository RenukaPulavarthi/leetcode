class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        d = {}
        ans = 0
        for j in range(len(s)):
            if s[j] not in d:
                d[s[j]] = 0
            d[s[j]] += 1
            maxFreq = max(d.values())
            currLength = j - i + 1
            if currLength - maxFreq > k:
                d[s[i]] -= 1
                i+=1
            ans = max(ans, j - i + 1)
        return ans
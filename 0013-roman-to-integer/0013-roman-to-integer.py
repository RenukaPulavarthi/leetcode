class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        curr = 0
        ans = 0
        for i in s[:: -1]:
            if curr > mapping[i]:
                curr -= mapping[i]
                ans += curr
                curr = 0
            else:
                ans += curr
                curr = mapping[i]
        return ans + curr
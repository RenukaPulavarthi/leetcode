class Solution:
    def largestEven(self, s: str) -> str:
        n = len(s)
        z = -1
        for i in range(n-1, -1, -1):
            if s[i] == '2':
                z = i
                break
        if z == -1:
            return ''
        return s[:z + 1]
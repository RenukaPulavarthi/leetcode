class Solution:
    def smallestNumber(self, n: int) -> int:
        ans = ""
        while n > 0:
            ans += "1"
            n = n >> 1
        return int(ans, 2)
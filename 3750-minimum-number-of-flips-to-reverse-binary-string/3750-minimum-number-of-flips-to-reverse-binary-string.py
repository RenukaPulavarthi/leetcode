class Solution:
    def minimumFlips(self, n: int) -> int:
        b = bin(n)[2::]
        i, j = 0, len(b)-1
        ans = 0
        while i < j:
            if b[i] != b[j]:
                ans += 2
            i += 1
            j -= 1
        return ans
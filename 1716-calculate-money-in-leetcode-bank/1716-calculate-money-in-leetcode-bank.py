class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        monday = 1
        while n > 0:
            for i in range(0, min(7, n)):
                ans += i + monday
            monday += 1
            n -= 7
        return ans

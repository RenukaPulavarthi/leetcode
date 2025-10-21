class Solution:
    def reverse(self, x: int) -> int:
        k = -1 if x < 0 else 1
        x = x * k
        rev = 0
        while x:
            rev = rev * 10 + (x % 10)
            x = x // 10
        return k * rev if k * rev >= -2**31 and k*rev < 2**31 else 0
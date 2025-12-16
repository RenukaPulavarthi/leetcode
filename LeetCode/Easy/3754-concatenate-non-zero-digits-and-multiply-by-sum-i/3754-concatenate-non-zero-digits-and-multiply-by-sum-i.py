class Solution:
    def sumAndMultiply(self, n: int) -> int:
        k = 0
        s = 0
        l = 0
        while n > 0:
            z = n % 10
            s += z
            if z != 0:
                k = z * (10 ** l) + k
                l += 1
            # print(z, k)
            n = n // 10
        return k * s
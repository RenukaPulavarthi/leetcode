class Solution:
    def reverse(self, x: int) -> int:
        neg_flag = False
        if x < 0:
            neg_flag = True
            x *= -1
        rev = 0
        while x > 0:
            rev = (rev * 10) + (x % 10)
            x = x // 10
        if neg_flag:
            rev *= -1
        return rev if rev >= -2 ** 31 and rev <= (2 ** 31 - 1) else 0
class Solution:
    def maxSumOfSquares(self, num: int, su: int) -> str:
        ans = ''
        for i in range(num):
            if su >= 9:
                ans += '9'
                su -= 9
            else:
                ans += str(su)
                su = 0
        if su != 0:
            return ''
        return ans
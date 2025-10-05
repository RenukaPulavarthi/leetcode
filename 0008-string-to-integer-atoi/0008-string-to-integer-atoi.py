class Solution:
    def myAtoi(self, s: str) -> int:
        ans = ""
        for i in s:
            if i == ' ':
                if len(ans) > 0:
                    break
                continue
            elif i.isdigit() or i == '.':
                ans += i
            elif i == '+' or i=='-':
                if len(ans) > 0:
                    break
                ans += i
            else:
                break
        sign = 1
        if len(ans) > 0 and ans[0].isdigit() == False:
            sign = 1 if ans[0] == '+' else -1
            ans = ans[1::]
        if len(ans) == 0:
            ans = "0"
        res = int(ans) * sign
        if res > 2**31 - 1:
            return 2**31 - 1
        if res < -2**31:
            return -2**31
        return res
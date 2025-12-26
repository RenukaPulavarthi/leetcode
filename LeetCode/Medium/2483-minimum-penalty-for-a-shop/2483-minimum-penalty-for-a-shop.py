class Solution:
    def bestClosingTime(self, customers: str) -> int:
        close = []
        cnt = 0
        for i in customers:
            if i == 'N':
                cnt += 1
            close.append(cnt)
        cnt = 0
        open = []
        for i in customers[::-1]:
            if i == 'Y':
                cnt += 1
            open.append(cnt)
        open = open[::-1]
        ans_pen = open[0]
        ans_idx = 0
        for i in range(1, len(customers)):
            curr_pen = close[i - 1] + open[i]
            if curr_pen < ans_pen:
                ans_pen = curr_pen
                ans_idx = i
        if ans_pen > close[-1]:
            ans_pen = close[-1]
            ans_idx = len(customers)
        return ans_idx

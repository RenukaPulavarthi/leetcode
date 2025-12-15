class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        prev = 0
        curr = 0
        for i in prices:
            if prev - 1 == i or prev == 0:
                curr += 1
            else:
                ans += ((curr * (curr + 1)) / 2)
                curr = 1
            prev = i
        ans += ((curr * (curr + 1)) / 2)
        return int(ans)



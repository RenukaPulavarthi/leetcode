class Solution:
    def minMoves(self, balance: List[int]) -> int:
        n = len(balance)
        neg = -1
        for i in range(n):
            if balance[i] < 0:
                neg = i
                break
        if neg == -1:
            return 0
        cost = []
        for i in range(n):
            cost.append([min(abs(neg - i), min(abs(i + n- neg), abs(neg + n - i))), balance[i]])
        cost.sort()
        print(cost)
        ans = 0
        tar = cost[0][1] * -1
        for i in cost[1::]:
            if tar == 0:
                break
            if i[1] >= tar:
                ans += (i[0] * tar)
                tar = 0
            else:
                ans += (i[0] * i[1])
                tar -= i[1]
        # print(tar)
        return ans if tar == 0 else -1
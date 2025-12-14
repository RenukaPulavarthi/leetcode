class Solution:
    def numberOfWays(self, corridor: str) -> int:
        ans = 1
        curr_s = 0
        bet = 1
        for i in corridor:
            if i == 'S':
                if curr_s < 2:
                    curr_s += 1
                else:
                    ans *= bet
                    bet = 1
                    curr_s = 1
            else:
                if curr_s == 2:
                    bet += 1
        if curr_s != 2:
            return 0
        return ans % (10**9 + 7)
                

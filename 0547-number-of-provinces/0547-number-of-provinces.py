class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = 0
        n = len(isConnected)
        visit = [0 for i in isConnected]

        def startVisit(idx):
            visit[idx] = 1
            for i in range(n):
                if isConnected[idx][i] == 1 and visit[i] == 0:
                    startVisit(i)
        
        for i in range(n):
            if visit[i] == 0:
                ans += 1
                startVisit(i)
        return ans
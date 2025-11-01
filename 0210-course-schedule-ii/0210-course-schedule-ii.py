class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for i in prerequisites:
            if i[0] not in adj:
                adj[i[0]] = []
            adj[i[0]].append(i[1])
        visited = [0 for i in range(numCourses)]
        ans = [False]
        res = []

        def dfs(idx):
            if ans[0] == True:
                return
            visited[idx] = 1
            if idx in adj:
                for i in adj[idx]:
                    if visited[i] == 1:
                        ans[0] = True
                        return
                    if visited[i] == 0:
                        dfs(i)
                        if ans[0] == True: return
            visited[idx] = 2
            res.append(idx)

        for i in range(numCourses):
            if visited[i] == 0:
                dfs(i)
                if ans[0] == True:
                    return []
        return res

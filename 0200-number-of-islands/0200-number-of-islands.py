def dfs(grid: List[List[int]], visited: List[List[int]], r: int, c: int) -> None:
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < len(grid) and nc < len(grid[0]) and grid[nr][nc] == "1" and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            dfs(grid, visited, nr, nc)
    return
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [ [0 for i in range(m)] for j in range(n) ]
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    # print(1)
                    ans += 1
                    visited[i][j] = 1
                    dfs(grid, visited, i, j)
        return ans
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        
        def dfs(idx, r, c):
            if idx >= len(word):
                return True
            dc = [0, 0, 1, -1]
            dr = [1, -1, 0, 0]
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if nc >= 0 and nc < m and nr >= 0 and nr < n and board[nr][nc] == word[idx]:
                    temp = board[nr][nc]
                    board[nr][nc]='@'
                    if dfs(idx+1, nr, nc): return True
                    board[nr][nc]=temp
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    temp = board[i][j]
                    board[i][j] = '#'
                    if dfs(1, i, j): return True
                    board[i][j] = temp
        return False
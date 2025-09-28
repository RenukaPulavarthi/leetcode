class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n, m = len(board), len(board[0])
        rows = {}
        cols = {}
        sub_mat = {}
        for i in range(n):
            for j in range(m):
                if board[i][j] == '.':
                    continue
                if i not in rows:
                    rows[i] = set()
                if j not in cols:
                    cols[j] = set()
                idx = (i // 3) * 3 + (j // 3)
                if idx not in sub_mat:
                    sub_mat[idx] = set()
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in sub_mat[idx]:
                    # print(rows,cols,sub_mat,board[i][j])
                    return  False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                sub_mat[idx].add(board[i][j])
        return True
                
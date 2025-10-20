from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        each = defaultdict(set)
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == '.': continue;
                idx_e = i // 3 * 3 + (j // 3)
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in each[idx_e]:
                    return False
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                each[idx_e].add(board[i][j])
        return True

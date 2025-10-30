from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        cols = defaultdict(set)
        rows = defaultdict(set)
        subpart = defaultdict(set)
        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                sub_idx = i // 3 * 3 + j // 3
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in subpart[sub_idx]:
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                subpart[sub_idx].add(board[i][j])
        return True
        
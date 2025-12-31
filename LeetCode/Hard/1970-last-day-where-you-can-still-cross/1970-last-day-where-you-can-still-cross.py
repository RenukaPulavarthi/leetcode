from collections import deque
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        l, r = 0, len(cells)
        ans = -1

        def isPosible(idx):
            arr = [[0 for i in range(col)] for j in range(row)]
            for i in range(idx):
                arr[cells[i][0] - 1][cells[i][1] - 1] = 1
            visited = [[False for i in range(col)] for i in range(row)]
            queue = deque()
            for i in range(col):
                if arr[0][i] == 0:
                    queue.append((0,i))
                    visited[0][i] = True
            dir = [ (0, 1), (0, -1), (1, 0), (-1, 0)]
            while len(queue) > 0:
                ele = queue.popleft()
                if ele[0] == row - 1:
                    return True
                for i in dir:
                    nr = ele[0] + i[0]
                    nc = ele[1] + i[1]
                    if 0 <= nr < row and 0 <= nc < col and visited[nr][nc] == False and arr[nr][nc] == 0:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
            return False
                    

        while l <= r:
            mid = (l + r) // 2
            if isPosible(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
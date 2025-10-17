class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m = m - 1
        n = n - 1
        mini = min(m, n)
        ans = 1
        for i in range(mini):
            ans = ans * (n + m - i) // (i + 1)
        return int(ans)
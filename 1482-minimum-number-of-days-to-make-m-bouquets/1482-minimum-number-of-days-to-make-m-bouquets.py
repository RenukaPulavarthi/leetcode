class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low, high = min(bloomDay), max(bloomDay)

        def solve(n):
            curr = 0
            cnt = 0
            for i in bloomDay:
                if i <= n:
                    curr += 1
                else:
                    cnt += (curr // k)
                    curr = 0
            cnt += (curr // k)
            return cnt >= m

        ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            # print(mid)
            if solve(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

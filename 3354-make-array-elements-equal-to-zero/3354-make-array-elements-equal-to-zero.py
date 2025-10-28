class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        def solve(idx, dire, lst):
            while 0 <= idx < n:
                if lst[idx] > 0:
                    lst[idx] -= 1
                    dire *= -1
                idx += dire
            
            return n == lst.count(0)
        
        for i in range(n):
            if nums[i] == 0:
                if solve(i, 1, nums[::]):
                    ans += 1
                if solve(i, -1, nums[::]):
                    ans += 1
        return ans
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d ={}
        curr = 0
        ans = 0
        d[0] = 1
        for i in nums:
            curr += i
            if curr - k in d:
                print(i,k,curr)
                ans += d[curr - k]
            if curr not in d:
                d[curr] = 0
            d[curr] += 1
        return ans

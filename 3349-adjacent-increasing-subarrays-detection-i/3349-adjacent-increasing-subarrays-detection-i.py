class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        pre = [-1 for i in nums]
        n = len(nums)
        for i in range(n-k+1):
            # print(i)
            for j in range(i+1, i+k):
                if nums[j-1] >= nums[j]:
                    # print(j)
                    break
            else:
                pre[i] = 1
        # print(pre)
        for i in range(n-k):
            #print(i, i+k)
            if pre[i] == 1 and pre[i+k] == 1:
                return True
        return False

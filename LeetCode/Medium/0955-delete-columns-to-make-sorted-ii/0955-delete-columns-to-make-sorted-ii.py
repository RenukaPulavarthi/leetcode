class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        ans = 0
        curr = ["" for i in range(len(strs))]
        for i in range(n):
            pre = curr[::]
            for j in range(len(strs)):
                pre[j] = pre[j] + strs[j][i]
            if sorted(pre) == pre:
                curr = pre
            else:
                ans += 1
        return ans
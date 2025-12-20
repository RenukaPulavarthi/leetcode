class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        k = len(strs[0])
        lst = [[] for i in range(k)]
        for i in strs:
            for j in range(k):
                lst[j].append(i[j])
        cnt = 0
        for i in lst:
            if sorted(i) != i:
                cnt += 1
        return cnt
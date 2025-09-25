class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start,end=intervals[0]
        ans=[]
        for i in intervals:
            if start<=i[0]<=end:
                end=max(i[1],end)
            else:
                ans.append([start,end])
                start,end=i
        ans.append([start,end])
        return ans

from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        d=Counter(s)
        heap=[(-d[i],i) for i in d]
        heapq.heapify(heap)
        ans=""
        prev=None
        while heap:
            curr=heapq.heappop(heap)
            ans+=curr[1]
            if prev is not None:
                heapq.heappush(heap,prev)
            if curr[0]<-1:
                prev=(curr[0]+1,curr[1])
            else:
                prev=None
            # print(prev,curr,heap,ans)
        if prev is not None:
            return ""
        return ans


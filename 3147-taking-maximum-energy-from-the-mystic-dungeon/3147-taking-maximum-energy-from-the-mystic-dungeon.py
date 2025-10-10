class Solution:
    def maximumEnergy(self, e: List[int], k: int) -> int:
        d={}
        ans=[]
        for i in range(len(e)):
            m=i%k
            if m in d:
                if d[m]+e[i]<e[i]:
                    d[m]=e[i]
                else:
                    d[m]+=e[i]
            else:
                d[m]=e[i]
        ans=min(e)-100
        print(d)
        for i in d:
            if d[i]>ans:
                ans=d[i]
        return ans;
                
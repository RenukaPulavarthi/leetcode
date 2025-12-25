class Solution:
    def maximumHappinessSum(self, l: List[int], k: int) -> int:
        l.sort()
        l=l[::-1]
        i=0
        s=0
        while(i<k):
            if l[i]-i>0:
                s+=l[i]-i
            i+=1
        return s;

class Solution:
    def climbStairs(self, n: int) -> int:
        a,b,c=0,1,0
        while(n):
            c=a+b
            a=b
            b=c
            n-=1
        return b
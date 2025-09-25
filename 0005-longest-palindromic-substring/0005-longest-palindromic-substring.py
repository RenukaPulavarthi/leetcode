class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp={}
        i=0
        for j in range(0,len(s)):
            i,k=0,j
            while i<len(s) and k<len(s):
                if i==k:
                    dp[(i,k)]=1
                elif i+1==k and s[i]==s[k]:
                    dp[(i,k)]=1
                elif s[i]==s[k] and (i+1,k-1) in dp:
                    dp[(i,k)]=1
                i+=1
                k+=1
        ans=""
        ans_l=0
        for i in dp:
            if i[1]-i[0]>ans_l:
                ans_l=i[1]-i[0]
                ans=s[i[0]:i[1]+1]
        return ans;
                
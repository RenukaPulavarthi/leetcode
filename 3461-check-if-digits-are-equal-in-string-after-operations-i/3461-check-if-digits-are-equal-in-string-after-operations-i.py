class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while(len(s)!=2):
            k=''
            for i in range(1,len(s)):
                k+=str((int(s[i])+int(s[i-1]))%10)
            # print(k)
            s=k
        # print(s)
        if s[0]!=s[1]:
            return False
        return True
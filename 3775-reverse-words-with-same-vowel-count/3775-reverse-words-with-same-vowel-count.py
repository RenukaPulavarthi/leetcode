class Solution:
    def reverseWords(self, s: str) -> str:
        lst = list(s.split())
        
        def vowel_count(s: str) -> int:
            cnt = 0
            for i in s:
                if i in 'aeiou':
                    cnt += 1
            return cnt
        
        ans = lst[0]
        tar = vowel_count(lst[0])
        for i in lst[1::]:
            ans += " "
            if vowel_count(i) == tar:
                ans += i[::-1]
            else:
                ans += i
        return ans
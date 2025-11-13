class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for i in strs[1::]:
            while not i.startswith(ans):
                ans = ans[:-1]
                if ans == "":
                    break
        return ans
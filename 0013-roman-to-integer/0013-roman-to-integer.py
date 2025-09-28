class Solution:
    def romanToInt(self, s: str) -> int:
        nums_map = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        curr = 0
        Number = 0
        for i in range(len(s)-1, -1, -1):
            if curr <= nums_map[s[i]]:
                Number += curr
                curr = nums_map[s[i]]
            else:
                curr -= nums_map[s[i]]
                Number += curr
                curr = 0
        Number += curr
        return Number
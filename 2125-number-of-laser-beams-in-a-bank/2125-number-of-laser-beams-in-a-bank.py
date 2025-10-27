class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev = 0
        for i in bank:
            ones = i.count("1")
            ans += (ones * prev)
            if ones > 0:
                prev = ones
        return ans
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        for i in complexity[1::]:
            if i <= complexity[0]:
                return 0
        ans = 1
        for i in range(1,len(complexity)):
            ans *= i
        return ans % (10**9+7)
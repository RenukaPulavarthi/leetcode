from collections import Counter
class Solution:
    def maxDistinct(self, s: str) -> int:
        d = Counter(s)
        return len(d)
        
class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        a_count, b_count = 0, 0
        for i in s:
            if i == "a":
                a_count += 1
            else:
                b_count += 1
        if a_count == b_count:
            return 0

        return abs(a_count - b_count)
import bisect
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        k=bisect.bisect_right(letters,target)
        if k<len(letters):
            return letters[k]
        return letters[0]
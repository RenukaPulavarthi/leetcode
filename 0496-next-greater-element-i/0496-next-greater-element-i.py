class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = []
        d = {}
        for i in nums2:
            while len(stack) > 0 and stack[-1] <= i:
                k = stack.pop()
                d[k] = i
            stack.append(i)
        for i in nums1:
            if i in d:
                ans.append(d[i])
            else:
                ans.append(-1)
        return ans

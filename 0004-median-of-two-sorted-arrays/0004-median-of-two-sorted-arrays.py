class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 = len(nums1), len(nums2)
        t = l1 + l2
        mid = t // 2
        i, j = 0, 0
        curr, prev = -1, -1
        itr = 0
        while itr <= mid:
            prev = curr
            if i < l1 and (j >= l2 or nums1[i] < nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1
            itr += 1
        if t % 2 == 1:
            return curr
        return (prev + curr) / 2
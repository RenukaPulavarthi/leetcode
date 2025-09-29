class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        br_pt = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                br_pt = i
                break
        if br_pt != -1:
            for i in range(len(nums) - 1, br_pt, -1):
                if nums[i] > nums[br_pt]:
                    nums[i], nums[br_pt] = nums[br_pt], nums[i]
                    break
        i = br_pt + 1
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return

        
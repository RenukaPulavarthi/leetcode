class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound():
            low, high = 0, len(nums)-1
            ans = -1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] >= target:
                    if nums[mid] == target:
                        ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans
        
        def upper_bound():
            low, high = 0, len(nums)-1
            ans = -1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] <= target:
                    if nums[mid] == target:
                        ans = mid
                    low = mid + 1
                else:
                    high = mid -1
            return ans
        return [lower_bound(), upper_bound()]
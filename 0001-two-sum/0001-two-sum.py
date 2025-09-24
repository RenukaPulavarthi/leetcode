class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i,j=0,len(nums)-1
        lst=[(nums[i],i) for i in range(len(nums))]
        lst.sort()
        while i<j:
            if lst[i][0]+lst[j][0]==target:
                return sorted([lst[i][1],lst[j][1]])
            elif lst[i][0]+lst[j][0]>target:
                j-=1
            else:
                i+=1
        return []
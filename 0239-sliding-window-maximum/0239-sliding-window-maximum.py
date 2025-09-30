from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        for i in range(k):
            while len(queue) > 0 and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
        ans=[]
        ans.append(queue[0])
        for i in range(k,len(nums)):
            while len(queue) > 0 and queue[-1] < nums[i]:
                queue.pop()
            # print(queue, nums[i])
            queue.append(nums[i])
            if queue[0] == nums[i-k]:
                queue.popleft()
            ans.append(queue[0])
        return ans
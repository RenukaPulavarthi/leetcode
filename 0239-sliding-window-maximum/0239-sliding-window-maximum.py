from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        ans = []
        n = len(nums)
        for i in range(k):
            while len(queue) > 0 and queue[-1] < nums[i]:
                queue.popleft()
            queue.append(nums[i])
        for i in range(k, n):
            ans.append(queue[0])
            if nums[i - k] == queue[0]:
                queue.popleft()
            while len(queue) > 0 and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
        ans.append(queue[0])
        print(i, queue)
        return ans
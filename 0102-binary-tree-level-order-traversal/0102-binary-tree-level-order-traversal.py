# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        if root is not None: queue.append([root])
        ans = []
        while len(queue) > 0:
            curr = []
            nxt = []
            for i in queue[0]:
                curr.append(i.val)
                if i.left is not None: nxt.append(i.left)
                if i.right is not None: nxt.append(i.right)
            ans.append(curr)
            queue.pop(0)
            if len(nxt) > 0: queue.append(nxt) 
        return ans

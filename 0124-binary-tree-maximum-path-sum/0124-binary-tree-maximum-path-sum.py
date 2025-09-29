# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [0]

        def solve(root):
            if root is None:
                return 0
            r = max(0, solve(root.right))
            l = max(0, solve(root.left))
            ans[0] = max(ans[0], r + l + root.val)
            return root.val + max(r, l)
        
        solve(root)
        return ans[0]
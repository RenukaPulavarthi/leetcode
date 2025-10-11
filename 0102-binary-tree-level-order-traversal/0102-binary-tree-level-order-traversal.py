# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        que = []
        que.append([root])
        while len(que) > 0:
            k = que.pop()
            curr = []
            curr_q = []
            for i in k:
                curr.append(i.val)
                if i.left is not None:
                    curr_q.append(i.left)
                if i.right is not None:
                    curr_q.append(i.right)
            ans.append(curr)
            if len(curr_q) > 0:
                que.append(curr_q)
        return ans



        
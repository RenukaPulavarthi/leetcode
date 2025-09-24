class Solution:
    def trap(self, height: List[int]) -> int:
        pre=[height[0]]
        for i in height[1::]:
            pre.append(max(pre[-1],i))
        post=[height[-1]]
        for i in range(len(height)-2,-1,-1):
            post.append(max(height[i],post[-1]))
        post=post[::-1]
        ans=0
        for i in range(len(height)):
            ans+=min(pre[i],post[i])-height[i]
        return ans
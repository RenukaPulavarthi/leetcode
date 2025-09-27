class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        m=[]
        while(i<=j):
            l=min(height[i],height[j])*(j-i)
            m.append(l)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max(m);
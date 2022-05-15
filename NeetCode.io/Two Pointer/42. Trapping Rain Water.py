# Runtime: 91 ms, faster than 98.26% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 15.7 MB, less than 60.74% of Python3 online submissions for Trapping Rain Water.

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        start = 0
        end = len(height)-1
        maxleft = 0
        maxright = 0
        while start<=end:
            if height[start]<height[end]:
                if maxleft>height[start]:
                    ans+=maxleft-height[start]
                else:
                    maxleft = height[start]
                start+=1
            else:
                if maxright>height[end]:
                    ans+=maxright-height[end]
                else:
                    maxright = height[end]
                end-=1
        return ans
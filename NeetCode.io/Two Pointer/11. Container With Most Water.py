# Runtime: 853 ms, faster than 63.16% of Python3 online submissions for Container With Most Water.
# Memory Usage: 27.4 MB, less than 89.88% of Python3 online submissions for Container With Most Water.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        ans = 0
        while start<end:
            ans = max(ans,min(height[start],height[end])*(end-start))
            if height[start]<height[end]:
                start+=1
            elif height[start]>height[end]:
                end-=1
            elif height[start]==height[end]:
                start+=1
                end-=1
        return ans
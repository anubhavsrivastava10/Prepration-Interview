# Runtime: 1437 ms, faster than 40.76% of Python3 online submissions for 3Sum.
# Memory Usage: 17.4 MB, less than 88.24% of Python3 online submissions for 3Sum.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited = set()
        ans = set()
        for i in range(len(nums)):
            if nums[i] not in visited:
                start = i+1
                end = len(nums)-1
                while start<end:
                    if nums[i]+nums[start]+nums[end]==0:
                        ans.add((nums[i],nums[start],nums[end]))
                        start+=1
                        end-=1
                    elif nums[i]+nums[start]+nums[end]<0:
                        start+=1
                    elif nums[i]+nums[start]+nums[end]>0:
                        end-=1
                visited.add(nums[i])
        return ans
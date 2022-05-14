# Runtime: 129 ms, faster than 93.13% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
# Memory Usage: 15 MB, less than 43.09% of Python3 online submissions for Two Sum II - Input Array Is Sorted.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1
        while start<end:
            if numbers[start]+numbers[end] == target:
                return [start+1, end+1]
            elif numbers[start]+numbers[end]<target:
                start+=1
            else:
                end-=1
        return []
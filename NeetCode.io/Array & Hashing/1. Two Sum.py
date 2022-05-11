# Runtime: 108 ms, faster than 81.88% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.1 MB, less than 96.56% of Python3 online submissions for Group Anagrams.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i in range(len(nums)):
            if target-nums[i] in hashtable:
                return [hashtable[target-nums[i]],i]
            else:
                hashtable[nums[i]] = i
        return []
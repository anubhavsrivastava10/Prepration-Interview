# Runtime: 490 ms, faster than 75.27% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 25.9 MB, less than 93.86% of Python3 online submissions for Contains Duplicate.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashtable = {}
        for item in nums:
            if item in hashtable:
                return True
            else:
                hashtable[item] = 1
        return False
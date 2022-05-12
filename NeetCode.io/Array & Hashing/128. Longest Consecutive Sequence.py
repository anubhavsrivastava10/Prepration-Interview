# Runtime: 399 ms, faster than 45.12% of Python3 online submissions for Longest Consecutive Sequence.
# Memory Usage: 32.6 MB, less than 10.20% of Python3 online submissions for Longest Consecutive Sequence.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashtable = {}
        res = 0
        for item in nums:
            if item not in hashtable:
                prev = hashtable.get(item-1,0)
                forw = hashtable.get(item+1,0)
                total = prev+forw+1
                hashtable[item] = total
                res = max(res,total)
                hashtable[item-prev] = total
                hashtable[item+forw] = total
        return res
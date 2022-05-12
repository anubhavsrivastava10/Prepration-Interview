# Runtime: 142 ms, faster than 46.38% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 18.7 MB, less than 39.89% of Python3 online submissions for Top K Frequent Elements.

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable = {}
        length = 0
        for item in nums:
            if item in hashtable:
                hashtable[item] += 1
            else:
                hashtable[item] = 1
        # print(hashtable)
        q = []
        for item in hashtable:
            length += 1
            heapq.heappush(q,(hashtable[item],item))
        # print(heappop(q))
        ans = []
        while True:
            # print(k-length,ans,q)
            if k-length==k:
                break
            if k-length>=0:
                element = heappop(q)
                ans.append(element[1])
            else:
                heappop(q)
            length-=1
        return ans
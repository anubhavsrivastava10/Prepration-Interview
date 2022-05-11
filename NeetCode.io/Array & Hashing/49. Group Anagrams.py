# Runtime: 108 ms, faster than 81.88% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.1 MB, less than 96.56% of Python3 online submissions for Group Anagrams.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = {}
        for item in strs:
            res = "".join(sorted(item))
            if res in hashtable:
                hashtable[res].append(item)
            else:
                hashtable[res] = [item]
        ans = []
        for item in hashtable:
            ans.append(hashtable[item])
        return ans
# Runtime: 52 ms, faster than 81.69% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.4 MB, less than 67.83% of Python3 online submissions for Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashtable = {}
        for item in s:
            if item in hashtable:
                hashtable[item] += 1
            else:
                hashtable[item] = 1
        
        for item in t:
            if item not in hashtable:
                return False
            hashtable[item] -= 1
        
        for item in hashtable:
            if hashtable[item]!=0:
                return False
        return True
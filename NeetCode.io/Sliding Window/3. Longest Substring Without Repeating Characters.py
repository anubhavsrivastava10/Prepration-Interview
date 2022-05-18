# Runtime: 70 ms, faster than 77.91% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.1 MB, less than 50.69% of Python3 online submissions for Longest Substring Without Repeating Characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        start = 0
        end = start+1
        visited = set()
        n = len(s)
        visited.add(s[start])
        ans = 1
        while end!=n:
            if s[end] in visited:
                ans = max(ans,end-start)
                visited.remove(s[start])
                start+=1
            else:
                visited.add(s[end])
                end+=1
        ans = max(ans,end-start)
        return ans
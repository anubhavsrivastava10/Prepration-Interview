# Runtime: 62 ms, faster than 56.89% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 14.4 MB, less than 86.19% of Python3 online submissions for Valid Palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        while start<end:
            # we could have also checked it with ord() by seeing there ASCII values
            if not s[start].isalpha() and not s[start].isdigit():
                start+=1
                continue
            if not s[end].isalpha() and not s[end].isdigit():
                end-=1
                continue
            if s[start].lower()==s[end].lower():
                start+=1
                end-=1
            else:
                return False
        return True
                
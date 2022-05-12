# https://www.lintcode.com/problem/659/

# 569 ms time cost
# 6.13 MB memory cost
# Your submission beats 89.60 % Submissions

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        ans = ""
        for item in strs:
            ans += '#'
            ans += item
            # ans += '#'
        return ans

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, strs):
        # write your code here
        ans = []
        i = 0
        count = 0
        val = ''
        for i in range(len(strs)):
            if strs[i]=='#':
                if count==0:
                    count+=1
                elif count==1:
                    if strs[i+1]!='#':
                        ans.append(val)
                        count = 1
                        val =""
                    else:
                        val+= strs[i]
            else:
                val += strs[i]
        ans.append(val)
        return ans
        
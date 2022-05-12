# Runtime: 230 ms, faster than 95.50% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 20.8 MB, less than 98.38% of Python3 online submissions for Product of Array Except Self.

# O(n) time complexity
# O(1) space

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        val = 1
        l = 0
        count0 = 0
        flag = 1
        for item in nums:
            l+=1
            if item != 0:
                val *= item
            else:
                count0 += 1
                flag = 0
        
        for i in range(l):
            if nums[i]!= 0:
                nums[i] = (val//nums[i])*flag
            else:
                if count0>1:
                    nums[i] = 0
                else:
                    nums[i] = val
        
        return nums
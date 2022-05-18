# Runtime: 1222 ms, faster than 63.01% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25 MB, less than 87.08% of Python3 online submissions for Best Time to Buy and Sell Stock.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        start = 0
        end = start+1
        while end!=len(prices):
            if prices[start]<=prices[end]:
                ans = max(ans, prices[end]-prices[start])
                end +=1
            elif prices[start]>prices[end]:
                start = end
                end = start+1
        return ans
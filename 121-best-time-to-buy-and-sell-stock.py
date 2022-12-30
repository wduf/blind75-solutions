# 95.81% time
# 38.92% memory

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, lo = 0, 100001
        for p in prices:
            if p < lo: 
                lo = min(lo, p)
            else:
                ans = max(ans, p - lo)
        return ans

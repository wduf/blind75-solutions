# kadane's algorithm
# 82.41% time
# 17.92% memory

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = cur = nums[0]
        skip = nums[1:]
        for n in skip:
            cur = max(n + cur, n)
            res = max(res, cur)
        return res

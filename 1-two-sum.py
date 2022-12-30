# 94.77% time
# 14.32% memory

class Solution:
    def twoSum(self, nums: List[int], t: int) -> list[int]:
        d = {}
        for i, n in enumerate(nums):
            if n in d:
                return [i, d[n]]
            d[t - n] = i

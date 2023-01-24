# 90.87% time
# 90.09% memory

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        res = [1 for _ in range(ln)]
        x = 1  # multiplication factor
        for i in range(ln):
            res[i] *= x
            x *= nums[i]
        x = 1
        for i in reversed(range(ln)):
            res[i] *= x
            x *= nums[i]
        return res

# 95.39% time
# 24.85% memory

class Solution:
    def search(self, nums: List[int], t: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) >> 1
            if nums[m] == t:
                return m
            if nums[m] < t:
                l = (m + 1)
            else:
                r = (m - 1)
        return -1

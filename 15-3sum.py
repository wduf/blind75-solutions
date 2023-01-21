# 56.74% time
# 89.85% memory

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if nums[0] > 0 or nums[-1] < 0:
            return []
        res = []
        for i, n in enumerate(nums):
            # don't want to use repeat starting nums
            if i and n == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                sm = n + nums[l] + nums[r]
                if sm < 0:
                    l += 1
                elif sm > 0:
                    r -= 1
                else:
                    # 3sum found
                    res.append((n, nums[l], nums[r]))
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
        return res

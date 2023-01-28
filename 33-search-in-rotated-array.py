# 90.26% time
# 15.23% memory

class Solution:
    def search(self, nums: List[int], t: int) -> int:
        # print("--------------------------")
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) >> 1
            # target found
            if nums[m] == t:
                return m
            # rotated
            if nums[m] > nums[r]:
                # between l and m
                if (nums[l] <= t) and (t < nums[m]):
                    r = m - 1
                else:
                    l = m + 1
            # no rotate or to the right of m
            else:
                # between m and r
                if (nums[m] < t) and (t <= nums[r]):
                    l = m + 1
                else:
                    r = m - 1
        return -1

# 85.02% time 
# 97.63% memory

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            m = (l + r) >> 1
            if isBadVersion(m):
                r = (m - 1)
            else:
                l = (m + 1)
        return l

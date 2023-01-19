# 96.11% time
# 47.88% memory

class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        l, r = [], []
        lo, hi = new_interval
        for cur in intervals:
            cur_lo, cur_hi = cur
            if lo > cur_hi:
                l.append(cur)
            elif hi < cur_lo:
                r.append(cur)
            else:
                lo, hi = min(lo, cur_lo), max(hi, cur_hi)
        return l + [[lo, hi]] + r

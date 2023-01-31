# 88.82% time 
# 25.32% time

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res, cur = [], intervals[0]
        for i in intervals[1:]:
            if cur[1] >= i[1]:
                continue
            if cur[1] >= i[0]:
                cur[1] = i[1]
            else:
                res.append(cur.copy())
                cur = i
        return res + [cur]

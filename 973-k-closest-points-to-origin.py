# 99.28% time
# 60.60% memory

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key = lambda x:(x[0] ** 2) + (x[1] ** 2))[:k]

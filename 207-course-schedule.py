# 73.55% time
# 14.37% memory

class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        d = {i:[] for i in range(n)}
        for c, p in pre:
            if c not in d:
                d[c] = []
            d[c].append(p)
        
        v = set()  # visited
        def dfs(c: int) -> bool:
            if not d[c]:
                return True
            if c in v:
                return False
            v.add(c)
            for p in d[c]:
                if not dfs(p):
                    return False
            v.remove(c)
            d[c] = []  # this course can be completed, no need to continue checking it
            return True
        
        # test all courses
        for c in d:
            if not dfs(c):
                return False
        return True

# 99.81% time
# 94.78% memory

class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        for c in set(r):
            if m.count(c) < r.count(c):
                return False
        return True

# 98.02% time
# 66.73% memory

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)) or (set(s) != set(t)):
            return
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        for c in t:
            if not d[c]:
                return False
            d[c] -= 1
        return not all(d.values())

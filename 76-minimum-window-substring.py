# 71.37% time
# 32.35% memory

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = None
        dh, dn = defaultdict(int), Counter(t)  # dict for have, dict for need
        cnth, cntn = 0, len(t)  # count for have, count for need
        l = 0
        for r in range(len(s)):
            if (cr := s[r]) in t:
                dh[cr] += 1
                cnth += int(dh[cr] <= dn[cr])
            while cnth == cntn:
                res = [l, r] if (not res) or ((r - l) < (res[1] - res[0])) else res
                if (cl := s[l]) in t:
                    dh[cl] -= 1
                    cnth -= int(dh[cl] < dn[cl])
                l += 1
        return s[res[0]:res[1] + 1] if res else ""

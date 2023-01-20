# 89.06% time
# 13.63% memory

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = l = r = 0
        cur = {c:False for c in set(s)}  # cur chars in sub
        for c in s:
            while cur[c]:
                cur[s[l]] = False
                l += 1
            else:
                cur[s[r]] = True
                r += 1
                res = max(res, r - l)
        return res

# 48.35% time
# 92.02% memory

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = l = r = 0
        cur = deque([])  # cur chars in sub
        for c in s:
            while c in cur:
                cur.popleft()
                l += 1
            else:
                cur.append(c)
                r += 1
                res = max(res, r - l)
        return res

# 21.98% time
# 92.02% memory

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 1
        res = 1
        while r <= len(s):
            sub = s[l:r]
            if len(sub) != len(set(sub)):
                l += 1
            else:
                res = max(res, r - l)
                r += 1
        return res

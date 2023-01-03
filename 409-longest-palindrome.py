# 73.84% time
# 64.33% memory

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        ans = 0
        odd = 0
        for c in s:
            if (c in d) and d[c]:
                d[c] = False
                ans += 2
                odd -= 1
            else:
                d[c] = True
                odd += 1
        return ans + (1 if odd else 0)

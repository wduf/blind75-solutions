# 95.94% time
# 40.84% memory

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ("".join(c for c in s if c.isalnum())).lower()
        return s == s[::-1]

# one-liner
# 85.98% time
# 97.90% space

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

# no built-ins
# 97.16% time
# 21.77% memory

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a), int(b)
        res = ""
        while x and y:
            s = (x % 10) + (y % 10)
            if s > 1:
                x += 10
                s -= 2
            res = str(s) + res
            x //= 10
            y //= 10
        while x:
            l = x % 10
            if l > 1:
                x += 10
                l -= 2
            res = str(l) + res
            x //= 10
        while y:
            l = y % 10
            if l > 1:
                y += 10
                l -= 2
            res = str(l) + res
            y //= 10
        return res if res else "0"

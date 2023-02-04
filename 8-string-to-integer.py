# 95.20% time
# 23.45% memory

class Solution:
    def myAtoi(self, s: str) -> int:
        # remove leading/trailing whitespace
        s = s.strip()
        # empty string
        if not s:
            return 0
        # get sign
        sign = 1
        if s[0] in ("-", "+"):
            if s[0] == "-":
                sign = -1
            s = s[1:]
        # convert to int
        res = 0
        for c in s:
            if not c.isdigit():
                break
            res = (10 * res) + int(c)
        # add sign
        res *= sign
        # clamp res
        int_min, int_max = -(1 << 31), (1 << 31) - 1
        if res < int_min:
            return int_min
        if res > int_max:
            return int_max
        return res

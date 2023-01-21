# 97.50% time
# 95.33% memory

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": lambda x, y: y + x,
            "-": lambda x, y: y - x,
            "*": lambda x, y: y * x,
            "/": lambda x, y: int(y / x)
        }
        stk = []
        for t in tokens:
            if t in ops:
                stk.append(ops[t](stk.pop(), stk.pop()))
            else:
                stk.append(int(t))
        return stk[0]

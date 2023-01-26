# 69.79% time
# 27.70% memory

class MinStack:
    def __init__(self):
        self.stk = []
        self.min = math.inf

    def push(self, val: int) -> None:
        self.min = min(self.min, val)
        self.stk.append((val, self.min))

    def pop(self) -> None:
        self.stk.pop()
        self.min = self.stk[-1][1] if self.stk else math.inf

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]

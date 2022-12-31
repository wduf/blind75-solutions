# 88.62% time
# 67.87% memory

class MyQueue:
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def dump(self) -> None:
        while self.stk1:
            self.stk2.append(self.stk1.pop())
    
    def fill(self) -> None:
        while self.stk2:
            self.stk1.append(self.stk2.pop())
        
    def push(self, x: int) -> None:
        self.dump()
        self.stk1.append(x)
        self.fill()

    def pop(self) -> int:
        # all calls guaranteed to be valid
        return self.stk1.pop()  # stack pop

    def peek(self) -> int:
        # all calls guaranteed to be valid
        return self.stk1[-1]  # stack peek

    def empty(self) -> bool:
        return not self.stk1

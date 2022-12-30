# 97.84% time
# 25.83% memory

class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            match c:
                case ")":
                    if stk and stk[-1] == "(":
                        stk.pop()
                    else:
                        return False
                case "]":
                    if stk and stk[-1] == "[":
                        stk.pop()
                    else:
                        return False
                case "}":
                    if stk and stk[-1] == "{":
                        stk.pop()
                    else:
                        return False
                case _:
                    stk.append(c)
        return not stk

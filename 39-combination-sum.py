# 86.95% time
# 92.37% memory

class Solution:
    def combinationSum(self, cands: List[int], t: int) -> List[List[int]]:
        
        def f(idx: int, sm: int) -> None:
            if sm == t:
                res.append(cur.copy())
                return
            if sm > t or idx >= ln_cands:
                return
            for i in range(idx, ln_cands):
                c = cands[i]
                cur.append(c)
                f(i, sm + c)
                cur.pop()
                
        ln_cands = len(cands)
        res, cur = [], []
        f(0, 0)
        return res

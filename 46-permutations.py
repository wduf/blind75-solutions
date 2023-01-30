# 74.08% time
# 19.99% memory

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def f() -> None:
            if len(used) == ln_nums:
                res.append(cur.copy())
                return
            for i, n in enumerate(nums):
                if i in used:
                    continue
                used.add(i)
                cur.append(n)
                f()
                used.remove(i)
                cur.pop()
        
        res, cur, used = [], [], set()
        ln_nums = len(nums)
        f()
        return res

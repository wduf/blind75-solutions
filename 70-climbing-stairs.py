# 91.30% time
# 56.93% memory

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def dfs(cur: int) -> int:
            if cur > n:
                return 0
            if cur == n:
                return 1
            if cur in memo:
                return memo[cur]
            memo[cur] = dfs(cur + 1) + dfs(cur + 2)
            return memo[cur]
        
        return dfs(0)

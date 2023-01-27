# 78.33% time
# 64.60% memory

class Solution:
    def numIslands(self, mtx: List[List[str]]) -> int:
        nr, nc = len(mtx), len(mtx[0])
        
        def dfs(r: int, c: int) -> None:
            # set this land to water (visited)
            mtx[r][c] = "0"
            # if adj tile in range and land
            if (r - 1 in range(nr)) and (mtx[r - 1][c] == "1"):
                dfs(r - 1, c)
            if (r + 1 in range(nr)) and (mtx[r + 1][c] == "1"):
                dfs(r + 1, c)
            if (c - 1 in range(nc)) and (mtx[r][c - 1] == "1"):
                dfs(r, c - 1)
            if (c + 1 in range(nc)) and (mtx[r][c + 1] == "1"):
                dfs(r, c + 1)   
        
        res = 0
        for r in range(nr):
            for c in range(nc):
                # land
                if mtx[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res

# dp
# 99.48% time
# 88.57% memory

class Solution:
    def updateMatrix(self, mtx: List[List[int]]) -> List[List[int]]:
        nr, nc = len(mtx), len(mtx[0])  # # of rows, # of cols
        for r in range(nr):
            for c in range(nc):
                if mtx[r][c] > 0:
                    up = mtx[r - 1][c] if (r > 0) else math.inf
                    left = mtx[r][c - 1] if (c > 0) else math.inf
                    mtx[r][c] = min(up, left) + 1
        for r in range(nr - 1, -1, -1):
            for c in range(nc - 1, -1, -1):
                if mtx[r][c] > 0:
                    down = mtx[r + 1][c] if (r < nr - 1) else math.inf
                    right = mtx[r][c + 1] if (c < nc - 1) else math.inf
                    mtx[r][c] = min(mtx[r][c], down + 1, right + 1)
        return mtx

# bfs
# 46.18% time
# 88.57% memory

class Solution:
    def updateMatrix(self, mtx: List[List[int]]) -> List[List[int]]:
        
        def inBounds(r: int, n: int) -> bool:
            return r in range(n)
        
        nr, nc = len(mtx), len(mtx[0])
        q = deque([])  # queue for bfs
        for r in range(nr):
            for c in range(nc):
                match mtx[r][c]:
                    case 0:
                        q.append((r, c))
                    case _:
                        mtx[r][c] = -1  # not processed
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))  # adjacent directions (relative)
        while q:
            r, c = q.popleft()
            for d in dirs:
                dr, dc = d  # delta r, delta c
                r1, c1 = r + dr, c + dc
                # out of bounds or already processed
                if (not inBounds(r1, nr)) or (not inBounds(c1, nc)) or (mtx[r1][c1] != -1):
                    continue
                mtx[r1][c1] = mtx[r][c] + 1
                q.append((r1, c1))
        return mtx

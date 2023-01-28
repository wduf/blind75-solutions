# 75.92% time
# 42.43% memory

class Solution:
    def orangesRotting(self, mtx: List[List[int]]) -> int:
        # count out from orange, as soon as lower found, stop
        # bfs w/ 2 stacks for and next oranges, once cur empty and next empty, return res if res else -1
        nr, nc = len(mtx), len(mtx[0])
        # no fresh oranges
        if not sum([mtx[r].count(1) for r in range(nr)]):
            return 0
        
        def f(r: int, c: int) -> None:
            # fresh orange found, make it rotten and add to q
            if (r - 1 in range(nr)) and (mtx[r - 1][c] == 1):
                mtx[r - 1][c] = 2
                q_nxt.append((r - 1, c))
            if (r + 1 in range(nr)) and (mtx[r + 1][c] == 1):
                mtx[r + 1][c] = 2
                q_nxt.append((r + 1, c))
            if (c - 1 in range(nc)) and (mtx[r][c - 1] == 1):
                mtx[r][c - 1] = 2
                q_nxt.append((r, c - 1))
            if (c + 1 in range(nc)) and (mtx[r][c + 1] == 1):
                mtx[r][c + 1] = 2
                q_nxt.append((r, c + 1))
        
        q_cur, q_nxt = deque([]), deque([])  # q_cur: current rotten oranges, q_nxt: next rotten oranges
        # add rotten oranges to q
        for r in range(nr):
            for c in range(nc):
                # add rotten orange to q_nxt
                if mtx[r][c] == 2:
                    q_nxt.append((r, c))
        res = -1
        # while more rotten oranges
        while q_nxt:
            # add next rotten oranges to cur rotten oranges, prepare for new bunch of rotten oranges in q_nxt
            q_cur, q_nxt = q_nxt, deque([])
            res += 1
            # go through all cur rotten oranges
            while q_cur:
                r, c = q_cur.popleft()
                f(r, c)
        # if still fresh oranges remaining, -1, else res
        return -1 if any([r.count(1) for r in mtx]) else res

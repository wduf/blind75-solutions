# 90.55% time
# 21.44% memory

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        fd = {i:{} for i in range(n)}  # flight dict
        for s, d, p in flights:
            fd[s][d] = p
        q = deque([(src, 0, k + 1)])  #  cur city, cur price, remaining stops + 1 (landing at dst counts as additional stop)
        v = {}  # visited
        res = math.inf
        while q:
            c, p, s = q.popleft()  # cur city, cur price, remaining stops
            # reached dst
            if c == dst:
                res = min(res, p)
                continue
            # too many stops
            if not s:
                continue
            # been here in less stops with lower price
            if (c in v) and (p >= v[c]):
                continue
            # update visited
            v[c] = p
            # next flight
            for f in fd[c]:
                # add flight with new price and one less stop
                q.append((f, p + fd[c][f], s - 1))
        return res if res != math.inf else -1

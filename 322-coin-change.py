# 99.70% time
# 33.61% memory

class Solution:
    def coinChange(self, coins: List[int], amt: int) -> int:
        if not amt:
            return 0
        q = deque([])  # queue
        for c in coins:
            q.append((amt, 0))
        v = set()  # visited
        while q:
            cur, cnt = q.popleft()
            if not cur:
                return cnt
            cnt += 1
            for c in coins:
                nxt = cur - c
                if (nxt in v) or (nxt < 0):
                    continue    
                q.append((nxt, cnt))
                v.add(nxt)
        return -1

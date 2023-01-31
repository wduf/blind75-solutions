# 98.10%
# 88.15%

class TimeMap:

    def __init__(self):
        self.d = defaultdict(lambda: defaultdict(int))
        self.prv = defaultdict(list)

    def set(self, k: str, v: str, t: int) -> None:
        self.d[k][t] = v
        self.prv[k].append(t)

    def get(self, k: str, t: int) -> str:
        # no prev vals or < smallest val
        if (not self.prv[k]) or (t < self.prv[k][0]):
            return ""
        # >= greatest val
        if t >= self.prv[k][-1]:
            return self.d[k][self.prv[k][-1]]
        # somewhere in the middle
        for i, n in enumerate(self.prv[k]):
            if n > t:
                return self.d[k][self.prv[k][i - 1]]

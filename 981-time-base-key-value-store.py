# 99.35% time
# 91.12% memory

class TimeMap:

    def __init__(self):
        self.d = defaultdict(lambda: defaultdict(int))

    def set(self, k: str, v: str, t: int) -> None:
        self.d[k][t] = v

    def get(self, k: str, t: int) -> str:
        cur_d = self.d[k]  # cur dict
        # NOTE: python dicts keep order of insertion, so we can iterate
        #       backwards through dict until largest time <= t is found
        for x in reversed(cur_d):
            if x <= t:
                return cur_d[x]
        # smaller than smallest val in cur dict
        return ""

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

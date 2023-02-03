# 82.90% time
# 25.92% memory

class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        
        def dfs(idx: int) -> bool:
            # got to end of s
            if idx == ln_s:
                return True
            # this idx leads to failure
            if idx in failed:
                return False
            # check all paths
            for i in d[idx]:
                if dfs(i):
                    return True
            # all paths fail, add to failure
            failed.add(idx)
            return False
        
        ln_s = len(s)
        # filter out words not in s
        words = [w for w in words if w in s]
        # fill index start, end dict
        d = defaultdict(list)
        for w in words:
            ln_w = len(w)
            # regex to check for all overlapping matches of w in s
            idxs = [m.start() for m in re.finditer(f"(?={w})", s)]
            for i in idxs:
                d[i].append(i + ln_w)
        # dfs w/ memo
        failed = set()
        return dfs(0)

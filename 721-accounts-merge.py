# 61.16% time
# 5.57% memory

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        def dfs(email: str) -> list[str]:
            # mark as visited
            visited.add(email)
            res = [email]
            # check all non-visited linked emails/nodes
            for e in g[email]:
                if e not in visited:
                    res += dfs(e)
            return res
        
        # create graph
        g = defaultdict(set)  # set or list works b/c visited
        for a in accounts:
            first,emails = a[1], a[2:]
            for e in emails:
                g[e].add(first)
                g[first].add(e)
        # run dfs on graph, fill res
        res, visited = [], set()
        for a in accounts:
            name, email = a[0], a[1]
            if email not in visited:
                res.append([name] + sorted(dfs(email)))
        return res

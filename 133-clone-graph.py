# 63.99% time
# 23.11% memory

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        clones = {}
        
        def f(p: 'Node') -> 'Node':
            if p.val not in clones:
                clones[p.val] = Node(p.val)
                for c in p.neighbors:
                    clones[p.val].neighbors.append(f(c))
            return clones[p.val]
        
        return f(node)

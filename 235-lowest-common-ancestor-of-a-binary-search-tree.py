# 99.47% time
# 23.99% memory

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # p < q
        if p.val > q.val:
            p, q = q, p
        lo, hi = p.val, q.val
        
        def lca(root: 'TreeNode') -> 'TreeNode':
            v = root.val
            if (lo <= v) and (hi >= v):
                return root
            return lca(root.right) if (lo > v) else lca(root.left)
        
        return lca(root)

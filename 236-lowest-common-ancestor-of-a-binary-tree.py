# 96.92% time
# 28.70% memory

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root: 'TreeNode') -> int:
            if not root:
                return 0
            score = int(root in (p, q)) + dfs(root.left) + dfs(root.right)
            if score == 2:
                nonlocal res
                res, score = root, 0
            return score
        
        res = None
        dfs(root)
        return res

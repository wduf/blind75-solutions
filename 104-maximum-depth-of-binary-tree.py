# 84.50% time
# 20.94% memory

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def f(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            l, r = f(root.left), f(root.right)
            return max(l, r) + 1
        
        return f(root)

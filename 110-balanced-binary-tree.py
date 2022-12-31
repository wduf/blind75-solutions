# 98.67% time
# 90.28% memory

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def f(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            lh = f(root.left)
            if lh == -1:
                return -1
            rh = f(root.right)
            if rh == -1:
                return -1
            return (1 + max(lh, rh)) if (abs(lh - rh) < 2) else -1
        
        return f(root) != -1

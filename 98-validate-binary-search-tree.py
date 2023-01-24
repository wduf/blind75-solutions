# 69.93% time
# 75.01% space

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def f(root: Optional[TreeNode], mn: int, mx: int) -> bool:
            if not root:
                return True
            v = root.val
            if (v <= mn) or (v >= mx):
                return False
            return f(root.left, mn, v) and f(root.right, v, mx)
        
        return f(root, -math.inf, math.inf)

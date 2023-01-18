# 90.04% time
# 38.43% memory

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def f(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            l, r = f(root.left), f(root.right)
            nonlocal res
            res = max(res, l + r)
            return max(l, r) + 1
    
        f(root)
        return res

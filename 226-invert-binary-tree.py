# 93.59% time
# 56.90% memory

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def f(root: Optional[TreeNode]) -> Optional[TreeNode]:
            if not root:
                return
            root.left, root.right = root.right, root.left
            f(root.left)
            f(root.right)
        
        f(root)
        return root

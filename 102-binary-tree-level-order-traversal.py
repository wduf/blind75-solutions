# 82.83% time
# 46.91% memory

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res, nxt = [], [root]
        while nxt:
            res.append([x.val for x in nxt])
            cur, nxt = nxt, []
            for x in cur:
                if x.left:
                    nxt.append(x.left)
                if x.right:
                    nxt.append(x.right)
        return res

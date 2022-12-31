# 98.38% time
# 14.84% memory

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:        
        start_color = image[sr][sc]
        # nothing to flood
        if start_color == color:
            return image
        
        def dfs(r: int, c: int) -> None:
            # out of bounds
            if (r not in range(len(image))) or (c not in range(len(image[0]))):
                return
            # not start color
            if image[r][c] != start_color:
                return
            # flood
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        dfs(sr, sc)
        return image

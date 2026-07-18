class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0

        visit = set()

        def dfs(r, c):

            if (r < 0 or r >= ROWS or c < 0 or c >= COLS 
                or (r, c) in visit or grid[r][c] == "0"):
                return
            
            directions = [[1, 0], [-1, 0], [0, 1], [0,-1]]
            visit.add((r,c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    islands += 1

        
        return islands
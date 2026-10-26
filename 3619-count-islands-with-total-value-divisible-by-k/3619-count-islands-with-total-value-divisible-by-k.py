class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        valid_islands = 0
        

        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == 0:
                return 0
                
            cell_val = grid[r][c]
            grid[r][c] = 0
            
            return (cell_val + 
                    dfs(r + 1, c) + 
                    dfs(r - 1, c) + 
                    dfs(r, c + 1) + 
                    dfs(r, c - 1))
                    
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    island_sum = dfs(r, c)
                    
                    if island_sum % k == 0:
                        valid_islands += 1
                        
        return valid_islands
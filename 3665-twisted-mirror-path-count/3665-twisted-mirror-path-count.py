class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        if m == 1 and n == 1:
            return 1 if grid[0][0] == 0 else 0
            
        R_in = [[0] * n for _ in range(m)]
        D_in = [[0] * n for _ in range(m)]
        
        if grid[0][0] == 0:
            if 1 < n: R_in[0][1] = 1
            if 1 < m: D_in[1][0] = 1
            
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                    
                in_r = R_in[r][c]
                in_d = D_in[r][c]
                
                if grid[r][c] == 0:
                    total_landed = (in_r + in_d) % MOD
                    
                    if c + 1 < n:
                        R_in[r][c+1] = (R_in[r][c+1] + total_landed) % MOD
                    if r + 1 < m:
                        D_in[r+1][c] = (D_in[r+1][c] + total_landed) % MOD
                else:
                    if r + 1 < m:
                        D_in[r+1][c] = (D_in[r+1][c] + in_r) % MOD
                    if c + 1 < n:
                        R_in[r][c+1] = (R_in[r][c+1] + in_d) % MOD
                        
        if grid[m-1][n-1] == 1:
            return 0
            
        return (R_in[m-1][n-1] + D_in[m-1][n-1]) % MOD
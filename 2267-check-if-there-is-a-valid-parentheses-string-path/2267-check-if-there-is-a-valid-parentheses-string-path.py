class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        if (m + n) % 2 == 0:
            return False
            
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
            
        dp = [0] * n
        dp[0] = 1 << 1 
        
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                    
                mask = 0
                if r > 0:
                    mask |= dp[c]
                if c > 0:
                    mask |= dp[c - 1]
                    
                if grid[r][c] == '(':
                    dp[c] = mask << 1
                else:
                    dp[c] = mask >> 1
                    
        return (dp[n - 1] & 1) != 0
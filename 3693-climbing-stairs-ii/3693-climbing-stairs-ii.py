class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        from typing import List
        p1 = 0
        p2 = float('inf')
        p3 = float('inf')
        
        for i in range(1, n + 1):
            current_cost = costs[i - 1]
            
            ans = p1 + current_cost + 1 
            
            if p2 != float('inf'):
                ans = min(ans, p2 + current_cost + 4) 
                
            if p3 != float('inf'):
                ans = min(ans, p3 + current_cost + 9) 
                
            p3, p2, p1 = p2, p1, ans
            
        return p1
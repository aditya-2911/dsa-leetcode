class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        strat1 = need1 * cost1 + need2 * cost2
        
        overlap = min(need1, need2)
        strat2 = overlap * costBoth + (need1 - overlap) * cost1 + (need2 - overlap) * cost2
        
        strat3 = max(need1, need2) * costBoth
        
        return min(strat1, strat2, strat3)
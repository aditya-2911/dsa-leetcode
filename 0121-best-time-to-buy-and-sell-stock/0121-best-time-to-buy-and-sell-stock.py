class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min=10**6
        max_profit=0

        for i in prices:
            if i<curr_min:
                curr_min=i
            profit=i-curr_min
            if profit>max_profit:
                max_profit=profit
        return max_profit
            
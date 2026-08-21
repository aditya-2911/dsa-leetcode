class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        import math
        n = len(coins)
        pie = []
        
        for mask in range(1, 1 << n):
            current_lcm = 1
            set_bits = 0
            
            for i in range(n):
                if mask & (1 << i):
                    current_lcm = math.lcm(current_lcm, coins[i])
                    set_bits += 1
                    
            sign = 1 if set_bits % 2 == 1 else -1
            pie.append((current_lcm, sign))
            

        def count_amounts(X: int) -> int:
            count = 0
            for lcm_val, sign in pie:
                count += sign * (X // lcm_val)
            return count

        low = 1
        high = min(coins) * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2

            if count_amounts(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num * 9:
            return ""
            
        count_9 = sum // 9
        remainder = sum % 9
        
        ans = "9" * count_9
        
        if count_9 < num:
            ans += str(remainder)
            
        zeros_needed = num - len(ans)
        ans += "0" * zeros_needed
        
        return ans
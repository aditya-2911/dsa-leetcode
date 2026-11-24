class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1 if nums[0] == 1 else 0
            
        ans = 2
        curr_prod = 1
        left = 0
        
        for right in range(n):
            while math.gcd(curr_prod, nums[right]) != 1:
                curr_prod //= nums[left]
                left += 1
                
            curr_prod *= nums[right]
            ans = max(ans, right - left + 1)
            
        return ans
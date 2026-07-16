import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        size=len(nums)
        prefixGcd=[0]*size

        currMax=0

        for i in range(size):
            if nums[i]>currMax:
                currMax=nums[i]
            prefixGcd[i]=math.gcd(nums[i], currMax)
        
        prefixGcd.sort()
        ans=0
        for i in range(size//2):
            ans+= math.gcd(prefixGcd[i], prefixGcd[size-1-i])
        
        return ans
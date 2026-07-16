import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        gcd=math.gcd
        size=len(nums)
        prefixGcd=[0]*size

        currMax=0

        for i, num in enumerate(nums):
            if num>currMax:
                currMax=num
            prefixGcd[i]=gcd(num, currMax)
        
        prefixGcd.sort()
        ans=0
        l,r=0,size-1
        while l<r:
            ans+= gcd(prefixGcd[l], prefixGcd[r])
            l+=1
            r-=1
        
        return ans
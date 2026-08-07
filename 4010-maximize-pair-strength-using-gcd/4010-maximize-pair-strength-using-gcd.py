from math import gcd

class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        size=len(nums)

        max_strength=0
        for i in range(size):
            for j in range(i+1,size):
                strength= (nums[i]*nums[j])//(gcd(nums[i], nums[j])**2)

                max_strength=max(max_strength, strength)

        return max_strength
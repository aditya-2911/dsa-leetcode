class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sumOfDigits(n):
            s=0
            while n:
                s+=n%10
                n//=10
            return s
        
        for i in range(len(nums)):
            if i==sumOfDigits(nums[i]):
                return i
        return -1
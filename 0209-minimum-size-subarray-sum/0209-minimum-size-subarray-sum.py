class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sumVal=0
        minLength=float('inf')
        flag=False
        low,high=0,0

        while high<len(nums):
            sumVal+=nums[high]
            while sumVal>=target:
                flag=True
                length=high-low+1
                minLength=min(minLength, length)

                sumVal-=nums[low]
                low+=1
            high+=1
        if flag:
            return minLength
        else: return 0
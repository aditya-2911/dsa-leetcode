class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, one, two=0,0,0

        for num in nums:
            if num==0: zero+=1
            elif num==1: one+=1
            else: two+=1
        
        for i in range(0,len(nums)):
            if i<zero:
                nums[i]=0
            elif i>=zero and i<zero+one:
                nums[i]=1
            else: nums[i]=2


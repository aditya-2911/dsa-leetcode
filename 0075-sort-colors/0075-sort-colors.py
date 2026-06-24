class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size=len(nums)
        leftPtr,mid,rightPtr=0,0,size-1

        while mid<=rightPtr:
            if nums[mid]==2:
                nums[mid],nums[rightPtr]=nums[rightPtr],nums[mid]
                rightPtr-=1
            
            elif nums[mid]==0:
                nums[leftPtr],nums[mid]=nums[mid],nums[leftPtr]
                leftPtr+=1
                mid+=1 
            
            else:
                mid+=1
            
        
                 


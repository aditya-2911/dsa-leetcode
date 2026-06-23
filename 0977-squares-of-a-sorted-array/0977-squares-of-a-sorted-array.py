class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squaredList = []
    
        leftPtr, rightPtr=0,len(nums)-1
        
        while leftPtr<=rightPtr:
            if nums[leftPtr]**2 >= nums[rightPtr]**2:
                squaredList.append(nums[leftPtr]**2)
                leftPtr+=1
            else:
                squaredList.append(nums[rightPtr]**2)
                rightPtr-=1
        squaredList.reverse()
        return squaredList

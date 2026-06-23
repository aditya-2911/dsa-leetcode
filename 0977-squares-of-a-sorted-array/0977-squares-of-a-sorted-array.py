class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        size=len(nums)
        squaredList = [0]*size

        leftPtr, rightPtr=0,size-1
        
        for num in range(size-1,-1,-1):
            if nums[leftPtr]**2 >= nums[rightPtr]**2:
                squaredList[num]=nums[leftPtr]**2
                leftPtr+=1
            else:
                squaredList[num]=nums[rightPtr]**2
                rightPtr-=1

        return squaredList

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size=len(nums)
        left=[1]*size

        for i in range(1,size):
            left[i]=left[i-1]*nums[i-1]
        
        curr_right=1

        for i in range(size-1,-1,-1):
            left[i]*=curr_right
            curr_right*=nums[i]

        return left
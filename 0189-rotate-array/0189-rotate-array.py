class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp=nums[:]

        for i in range(len(temp)):
            nums[(i+k)%len(temp)]=temp[i]
        
        